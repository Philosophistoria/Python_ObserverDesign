
import contextlib

class ObservableNotifier:
    def __init__(self, notifier, callback=None):
        self.callbacks = [] 
        self.notifier = notifier
        self.attatch(callback)

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

        # return a wrapper which yield generator of iterator of attr executing callbacks before/after the yielding
        if callable(self.attr):
            return self.__wrapper
        else:
            return self.__wrapper_uncallable

    def __default_action(self, *args):
        print ('no such attribute')
        raise AttributeError

    @contextlib.contextmanager
    def __wrapper(self, *args):
        for callback in self.callbacks:
            callback(self.attr_name, "pre")

            yield self.attr(*args)

        for callback in self.callbacks:
            callback(self.attr_name, "post")
    
    @property
    @contextlib.contextmanager
    def __wrapper_uncallable(self):
        for callback in self.callbacks:
            callback(self.attr_name, "pre")

            yield self.attr

        for callback in self.callbacks:
            callback(self.attr_name, "post")