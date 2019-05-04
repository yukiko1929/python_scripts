x = 100

def func1():
    print(x)

def func2():
    x = 'yukiko'
    print(x)

def func3():
    global x
    x = 100000
    print(x)

print(x)
func1()
func2()
func3()
print(x)