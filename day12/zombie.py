import os
import time

print('starting')

retval = os.fork()
if retval:
    print('parent process')
    time.sleep(60)  # after parent process ends, systemd will take over zombie process and end them
else:
    print('child process')
    time.sleep(15)     # sleep shorter time than parent process. after 15s, it becomes zombie process
    exit()     #

print('done')


# watch -n1 ps a
