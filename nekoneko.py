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
        return "nyaan"

    def meow(self):
        return "meow"

    def default_response(self):
        return "wagahai am neko"


class NekoObserver:
    def __init__(self, buf=[None]):
        self.buf = buf

    def listen(self, nakigoe):
        if (nakigoe == "meow"):
            print("this nekosama meows!")
            print(self.buf)
        else:
            print("this nekosama is from Japan")
            print(self.buf)

# Usage
if __name__ == "__main__":
    print("\n! Ordinal neko:\n")
    neko = Neko()
    print(neko.nyan())
    print(neko.meow())
    # neko.neee()           # <-- AttributeError: 'Neko' object has no attribute 'neee'
    # neko.nyan("nekoneko") # <-- TypeError: nyan() takes 1 positional argument but 2 were given

    print("\n! noko dignosis:\n")
    retval = [None]
    nekodignosis = NekoObserver(retval)
    heroic_neko = HeroicNotifier(neko)
    heroic_neko.attatch(nekodignosis.listen)
    retval[0] = heroic_neko.nyan()
    retval[0] = heroic_neko.meow()

    print("\n! neko dont have neee voice:\n")
    retval[0] = heroic_neko.neee()

    # heroic_neko.nyan("nyaaaan") # <-- TypeError: nyan() takes 2 positional argument but 2 were given