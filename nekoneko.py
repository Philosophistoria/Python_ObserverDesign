class HeroicNotifier:
    def __init__(self, notifier, callback=None):
        self.callbacks = [] 
        self.notifier = notifier
        self.attatch(callback)

    def attatch(self, callback):
        if (callable(callback)):
            self.callbacks.append(callback)

    def __getattr__(self, name):
        for callback in self.callbacks:
            callback(name)
        if hasattr(self.notifier, name):
            return getattr(self.notifier, name)
        elif hasattr(self.notifier, "default_response"):
            return getattr(self.notifier, "default_response")
        else:
            return self.__default_action
            # same as:
            # return getattr(self, "__default_action")

    def __default_action(self, *args):
        print ('no such attribute')


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