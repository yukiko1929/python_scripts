class Weapon:
    def __init__(self, name, level):
        self.name = name
        self.level = level

class Fighter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, cotent):
        print('I am %s, %s' % (self.name, cotent))

    def drink(self, drinks):
        print('I am %s, I drink %s' %(self.name, drinks))

    def entertain(self, activity):
        print('I am %s, %s is my hobby' % (self.name, activity))

if __name__ == '__main__':
    w = Weapon('toyako', 10000)
    sakada = Fighter('sakada', w)
    print(sakada.weapon)
    print(sakada.weapon.name, sakada.weapon.level)
    # sakada = Fighter('坂田銀時', '洞爺湖')   # to call init function automatically
    # katsura = Fighter('桂小太郎','ヅラ')
    # print('名前は%s, %sを武器として使っています' % (sakada.name, sakada.weapon))
    # print('名前は%s, %sを武器として使っています' % (katsura.name, katsura.weapon))
    # sakada.speak('お金を貸してもらいますか？')
    # sakada.drink('strawberry milk')
    # sakada.entertain('reading')

# __init__ is a struction method, which will be called automatically upon instance
# method ---- the functions within class
# during instance, the instance will be passwd to __init__ function as the first parameter
# self is ony a variable, it can be another one. in Python usually we use 'self'
#


