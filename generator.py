def decorate(func1):
    def red():
        return '\033[31;1m%s\033[0m' % func1

    return red

#@decorate
def hello():
    return 'hello yukiko'

def yukiko():
    return 'hahahhahhah'

if __name__ == '__main__':
    print(yukiko())
    a = decorate(yukiko())
    print(a())
    b = decorate(hello())
    print(b())