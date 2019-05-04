days = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_days = [31,29,31,30,31,30,31,31,30,31,30,31]

year = int(input('year:'))
month = int(input('month(1-12):'))
day = int(input('day:(1-31)'))

if [year % 4 == 0 and year % 100 != 0] or [year % 400 == 0]:
    day_so_far = leap_days[0:month-1]
    month_count = 0
    for sepe in day_so_far:
        month_count += sepe
    print('it is the %s day in %s' % (month_count + day, year))
else:
    day_so_far = days[0:month - 1]
    month_count = 0
    for sepe in day_so_far:
        month_count += sepe
    print('it is the %s day in %s' % (month_count + day, year))