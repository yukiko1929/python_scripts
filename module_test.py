def find_number():
    import math
    for i in range(100000):
        cal1 = int(math.sqrt(i + 100))
        cal2 = int(math.sqrt(i + 268))
        if cal1 * cal1 == i + 100 and cal2 * cal2 == i + 268:
            print(i)

greeting = 'hello yukiko'

def pstar(n=50):
    print('*' * n)

if __name__ == '__main__':
    pstar()
    pstar(70)

#if __name__ == '__main__':
