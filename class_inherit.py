class Fighter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, contents):
        print('I am %s, %s' % (self.name, contents))

class MaleFighter(Fighter):
    pass

class FemaleFighter(Fighter):
    pass

    def speak(self, contents):
        print('I am FF %s, code 996.%s' % (self.name, contents))

    def waza(self, wazaname, kill):
        print('I am FFF %s, I can kill %s one time with %s ' % (self.name, kill, wazaname))


if __name__ == '__main__':
    sakada = MaleFighter('sakada', 'toyako')
    sakada.speak('how you doing')

    hitomi = FemaleFighter('hitomi', 'eyes')
    hitomi.speak('一遍、死んでみる？')
    hitomi.waza('one glance', 10 )