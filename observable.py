
import contextlib

class ObservableNotifier:
    def __init__(self, notifier, returningtype='functionref', callback=None):
        # notifier: is object to be wrapped
        # returningtype: 
        #   if it is 'contextmanager', 
        #       the wrapped notifier methods is returnd as contextmanager so it should be used with the 'with' statement;
        #       the retval is yielded in it and can be received as var after 'as' keyword;
        #       after yielding (post with statement) the post-callbacks are executed
        #   else (default)
        #       the wrapped notifier methods is returned as reference, so it can executed with '()'
        #       the retval is returned after the post-callbacks are executed
        #       if the attribute is not callable (if not method) just return the attribute reference
        self.callbacks = [] 
        self.notifier = notifier
        self.attatch(callback)
        if (type(returningtype) == str and returningtype == 'contextmanager'):
            self.rettype = 'contextmanager'
        else:
            self.rettype = 'functionref'

    def attatch(self, callback):
        if (callable(callback)):
            self.callbacks.append(callback)

    def __getattr__(self, name):
        # Set attr_name
        self.attr_name = name 

        # Set the reference to the entity of the attr
        self.attr = self.__default_action
        if hasattr(self.notifier, self.attr_name):
            self.attr = getattr(self.notifier, self.attr_name)
        elif hasattr(self.notifier, "default_response"):
            self.attr = getattr(self.notifier, "default_response") 

        if self.rettype == 'contextmanager':
            # return a wrapper which yield generator of iterator of attr executing callbacks before/after the yielding
            if callable(self.attr):
                return self.__wrapper_cm
            else:
                return self.__wrapper_cm_uncallable
        else:
            if callable(self.attr):
                return self.__wrapper
            else:
                return self.attr


    def __default_action(self, *args):
        print ('no such attribute')
        raise AttributeError

    def __wrapper(self, *args):
        for callback in self.callbacks:
            callback(self.attr_name, "pre")

        tmp = self.attr(*args)

        for callback in self.callbacks:
            callback(self.attr_name, "post")

        return tmp

    @contextlib.contextmanager
    def __wrapper_cm(self, *args):
        for callback in self.callbacks:
            callback(self.attr_name, "pre")

        yield self.attr(*args)

        for callback in self.callbacks:
            callback(self.attr_name, "post")
    
    @property
    @contextlib.contextmanager
    def __wrapper_cm_uncallable(self):
        for callback in self.callbacks:
            callback(self.attr_name, "pre")

        yield self.attr

        for callback in self.callbacks:
            callback(self.attr_name, "post")
