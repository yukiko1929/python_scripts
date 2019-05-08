import os
import threading
import time

def add():
    result = 0
    for i in range(1,20000001):
        result += i
    print(result)

if __name__ == '__main__':
# one process, one thread
    start1 = time.time()
    for i in range(2):
        add()
    end1 = time.time()
    print(end1 - start1)

# to use 2 processes
    start2 = time.time()
    for i in range(2):
        retval = os.fork()
        if retval == 0:
            add()
            exit()
    for i in range(2):
        os.waitpid(-1, 0)   #hang up parent process twice. wait the child process to end
    end2 = time.time()      # without hang up the parent process, this time would only count fork_creating time
    print(end2 - start2)

# to start 2 threads
    start3 = time.time()
    t1 = threading.Thread(target=add)
    t1.start()
    t2 = threading.Thread(target=add)
    t2.start()
    t1.join()    #hang up parent process
    t2.join()    #hang up parent process
    end3 = time.time()
    print(end3 - start3)
