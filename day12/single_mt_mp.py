import time
import subprocess
import threading
import os

def number_add():
    result = 0
    for i in range(1,20000001):
        result += i
    print(result)

if __name__ == '__main__':
    start1 = time.time()
    for i in range(2):
        number_add()
    end1 = time.time()
    print(end1 - start1)

    start2 = time.time()
    for i in range(2):
        retval = os.fork()
        if not retval:
            number_add()
            exit()
    for i in range(2):
        os.waitpid(-1, 0)
    end2 = time.time()
    print(end2 - start2)

    start3 = time.time()
    t1 = threading.Thread(target=number_add)
    t1.start()
    t2 = threading.Thread(target=number_add)
    t2.start()
    t1.join()
    t2.join()
    end3 = time.time()
    print(end3 - start3)