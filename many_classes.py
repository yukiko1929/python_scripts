class AA:
    def func1(self):
        print('AA func1')

    def general(self):
        print('AA general')

class BB:
    def func2(self):
        print('BB func2')

    def general(self):
        print('BB genral')

class CC:
    def func3(self):
        print('CC func3')

    def general(self):
        print('DD genral')

class DD(BB, CC, AA):
    pass
    # def general(self):
    #     print('self general')

if __name__ == '__main__':
    d = DD()
    d.func1()
    d.func2()
    d.func3()
    d.general()
