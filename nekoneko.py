import contextlib

class HeroicNotifier:
    def __init__(self, notifier, callback=None):
        self.callbacks = [] 
        self.notifier = notifier
        self.attatch(callback)

    def attatch(self, callback):
        if (callable(callback)):
            self.callbacks.append(callback)

    def __getattr__(self, name):
        self.attr_name = name 
        return self.__wrapper

    def __default_action(self, *args):
        print ('no such attribute')

    def __wrapper(self, *args):
        if hasattr(self.notifier, self.attr_name):
            self.callable_attr = getattr(self.notifier, self.attr_name)
        elif hasattr(self.notifier, "default_response"):
            self.callable_attr = getattr(self.notifier, "default_response")
        else:
            self.callable_attr = self.__default_action
            # same as:
            # getattr(self, "__default_action")

        retval = None

        for callback in self.callbacks:
            callback(self.attr_name)

        retval = self.callable_attr(*args)

        for callback in self.callbacks:
            callback(self.attr_name)

        return retval

        

class Neko:
    def nyan(self):
        print("nyaan")

    def meow(self):
        print("meow")

    def default_response(self):
        print ("wagahai am neko")


class NekoObserver:
    def listen(self, nakigoe):
        if (nakigoe == "meow"):
            print("this nekosama meows!")
        else:
            print("this nekosama is from Japan")

# Usage
if __name__ == "__main__":
    print("\n! Ordinal neko:\n")
    neko = Neko()
    neko.nyan()
    neko.meow()
    # neko.neee()           # <-- AttributeError: 'Neko' object has no attribute 'neee'
    # neko.nyan("nekoneko") # <-- TypeError: nyan() takes 1 positional argument but 2 were given

    print("\n! noko dignosis:\n")
    nekodignosis = NekoObserver()
    heroic_neko = HeroicNotifier(neko)
    heroic_neko.attatch(nekodignosis.listen)
    heroic_neko.nyan()
    heroic_neko.meow()

    print("\n! neko dont have neee voice:\n")
    heroic_neko.neee()

    # heroic_neko.nyan("nyaaaan") # <-- TypeError: nyan() takes 2 positional argument but 2 were given