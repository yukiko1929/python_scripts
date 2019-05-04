class Weapon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Fighter:
    def __init__(self, name, wname, wlevel):
        self.name = name
        self.weapon = Weapon(wname, wlevel)

if __name__ == '__main__':
    lb = Fighter('sakada', 'toyako', 10000)
    print('name: %s, weapon: %s, level: %s'  % (lb.name, lb.weapon.name, lb.weapon.level))