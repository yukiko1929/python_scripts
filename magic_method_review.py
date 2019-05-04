# class MagicMethod:
#     def __init__(self, title, author, publisher):
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#
#     def __str__(self):
#         return 'the book %s is written by %s and published by %s' % (self.title, self.author, self.publisher)
#
#     def __call__(self):
#         print('the book %s is written by %s and published by %s' % (self.title, self.author, self.publisher))
#
# if __name__ == '__main__':
#     nakayama = MagicMethod('good weather', 'nakayama', 'penguin')
#     print(nakayama)
#     nakayama()

class AA:
    def func1(self):
        print('AA function')

    def func(self):
        print('the function from AA')

class BB:
    def func2(self):
        print('BB function')

class CC:
    def func3(self):
        print('CC')

class DD(AA, BB, CC):
    pass
    # def fun4(self):
    #     print('DD')
    def func(self):
        print('the function from DD')

if __name__ == '__main__':
    haha = DD()
    haha.func3()
    haha.func()