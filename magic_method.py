# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def __str__(self):
#         return '%s' % self.title
#
#     def __call__(self):
#         print('the book %s is written by %s' % (self.title, self.author))
#
#
# if __name__ == '__main__':
#     corepython = Book('Python core programming', 'Wesley')
#     print(corepython)
#     corepython()

class Hotel:
    def __init__(self, fees, days):
        self.fees = fees
        self.days = days

    def ordinary(self):
        one_day = int(self.fees) + 15
        all_sum = one_day * self.days * 0.9
        return all_sum

    def membership(self):
        one_day = int(self.fees) + 15
        all_sum = one_day * self.days
        return all_sum

if __name__ == '__main__':
    hotel = Hotel(500,30)
    print(hotel.ordinary())
    print(hotel.membership())
