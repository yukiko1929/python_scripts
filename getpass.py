import getpass
all_department = ['development','mass_production','finance']
name = input('please enter your name:')
department = input('your department:')
superior = input('your superior:')
salary = float(getpass.getpass('please enter your salary:'))

if department in all_department:
    if salary > 100000.82:
        print('hopeful')
    else:
        print('hopeless poor guy')