# The symbolic link of observable.py is in Test dir
import observable

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

    def listen(self, *args):
        if (args[0] == "meow"):
            print("this nekosama meows!", args)
            print(self.buf)
        else:
            print("this nekosama is from Japan", args)
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
    heroic_neko = observable.ObservableNotifier(neko)
    heroic_neko.attatch(nekodignosis.listen)
    with heroic_neko.nyan() as whatnekosays:
        retval[0] = whatnekosays
    with heroic_neko.meow() as whatnekosays:
        retval[0] = whatnekosays
    print(heroic_neko.voice)
    with heroic_neko.voice as whatnekosays:
        retval[0] = whatnekosays

    print("\n! neko dont have neee voice:\n")
    with heroic_neko.neee() as whatnekosays:
        retval[0] = whatnekosays

    # heroic_neko.nyan("nyaaaan") # <-- TypeError: nyan() takes 2 positional argument but 2 were given