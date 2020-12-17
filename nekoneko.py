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
        # Set attr_name
        self.attr_name = name 

        tmp = self.__default_action
        if hasattr(self.notifier, self.attr_name):
            tmp = getattr(self.notifier, self.attr_name)
        elif hasattr(self.notifier, "default_response"):
            tmp = getattr(self.notifier, "default_response") 

        if callable(tmp):
            self.callable_attr = tmp
        # if the attribute required was not callback just return the ref.
        else:
            return tmp

        return self.__wrapper

    def __default_action(self, *args):
        print ('no such attribute')
        raise AttributeError

    @contextlib.contextmanager
    def __wrapper(self, *args):
        for callback in self.callbacks:
            callback(self.attr_name)

        yield self.callable_attr(*args)

        for callback in self.callbacks:
            callback(self.attr_name)

        

class Neko:
    def __init__(self):
        self.voice = "he is john"
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
    with heroic_neko.nyan() as whatnekosays:
        retval[0] = whatnekosays
    with heroic_neko.meow() as whatnekosays:
        retval[0] = whatnekosays
    print(heroic_neko.voice)

    print("\n! neko dont have neee voice:\n")
    with heroic_neko.neee() as whatnekosays:
        retval[0] = whatnekosays

    # heroic_neko.nyan("nyaaaan") # <-- TypeError: nyan() takes 2 positional argument but 2 were given