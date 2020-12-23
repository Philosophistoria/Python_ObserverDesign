
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
        # Set the reference to the entity of the attr
        attr = self.__default_action
        if hasattr(self.notifier, name):
            attr = getattr(self.notifier, name)
        elif hasattr(self.notifier, "default_response"):
            attr = getattr(self.notifier, "default_response") 

            # return a wrapper which yield generator of iterator of attr executing callbacks before/after the yielding
        if callable(attr):
            if self.rettype == 'contextmanager':
                @contextlib.contextmanager
                def __wrapper_cm(*args):
                    for callback in self.callbacks:
                        callback(None, name, "pre")

                    retval = attr(*args)
                    yield retval

                    for callback in self.callbacks:
                        callback(retval, name, "post")
                return __wrapper_cm
            # if the attr is not callable, yield the attr ref
            else:
                def __wrapper(*args):
                    for callback in self.callbacks:
                        callback(None, name, "pre")

                    retval = attr(*args)

                    for callback in self.callbacks:
                        callback(retval, name, "post")

                    return retval
                return __wrapper
        else:
            return attr


    def __default_action(self, *args):
        print ('no such attribute')
        raise AttributeError


    
