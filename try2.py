# to practice try and except
try:
    num = int(input('please input a number'))
    num2 = 100 / num
#    print(num2)

# except ZeroDivisionError:
#     print('the number can not be zero')
# except KeyboardInterrupt:
#     print('\nbye-bye')
# except ValueError:
#     print('invalid input')
# except EOFError:
#     print('\nbye-bye')
except (ZeroDivisionError, ValueError):
    print('invalid input')
except (KeyboardInterrupt, EOFError):
    print('\nbye-bye')
    exit()

else:              #
    print(num2)

finally:
    print('done')