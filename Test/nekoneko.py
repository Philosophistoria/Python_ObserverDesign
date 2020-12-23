
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
'''
pyobservable/../$ python3 -m Test.nekoneko
'''

if __name__ == "__main__":
    import os   #nopep
    import sys  #nopep
    sys.path.append('../')
    from pyobservable import observable #nopep
    from pyobservable import observer #nopep

    print("\n! Ordinal neko:\n")
    neko = Neko()
    print(neko.nyan())
    print(neko.meow())
    # neko.neee()           # <-- AttributeError: 'Neko' object has no attribute 'neee'
    # neko.nyan("nekoneko") # <-- TypeError: nyan() takes 1 positional argument but 2 were given

    print("\n --- ! w/ with statement --- ")
    print("\n! noko dignosis:\n")
    retval = [None]
    nekodignosis = NekoObserver(retval)
    heroic_neko = observable.ObservableNotifier(neko,'contextmanager')
    heroic_neko.attatch(observer.receive_notification_by(nekodignosis.listen,funcreqarg=2))

    with heroic_neko.nyan() as whatnekosays:
        retval[0] = whatnekosays
    print()

    with heroic_neko.meow() as whatnekosays:
        retval[0] = whatnekosays
    print()

    print(heroic_neko.voice)
    with heroic_neko.voice as whatnekosays:
        retval[0] = whatnekosays
    print()

    print("\n! neko dont have neee voice:\n")
    with heroic_neko.neee() as whatnekosays:
        retval[0] = whatnekosays
    print()

    # heroic_neko.nyan("nyaaaan") # <-- TypeError: nyan() takes 2 positional argument but 2 were given
    
    print("\n --- ! w/o with statement --- ")
    print("\n! noko dignosis:\n")
    retval = [None]
    nekodignosis = NekoObserver(retval)
    heroic_neko = observable.ObservableNotifier(neko,'functionref')
    heroic_neko.attatch(observer.receive_notification_by(nekodignosis.listen,timing_res='post',attr_res='all',funcreqarg=2))

    retval[0] = heroic_neko.nyan()
    print()

    retval[0] = heroic_neko.meow()
    print()

    print(heroic_neko.voice)
    retval[0] = heroic_neko.voice
    print()

    print("\n! neko dont have neee voice:\n")
    retval[0] = heroic_neko.neee()
    print()