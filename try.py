try:
    number = int(input('please input a number:'))
    result = 100 / number
    #print(result)

# except ValueError:
#     print('invalid input')
# except ZeroDivisionError:
#     print('invalid number')
# except EOFError:
#     print('\nGoodbye')
#     exit()
# except KeyboardInterrupt:
#     print('\nbye-bye')
#     exit()

except (ValueError, ZeroDivisionError):
    print('invalid input')
except(KeyboardInterrupt, EOFError):
    print('\nBye-bye')

else:
    print(result)
finally:
    print('done')
