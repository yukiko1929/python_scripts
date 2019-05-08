# import os
# import time
#
# print('loading')
# retval = os.fork()
# if retval:
#     print('parent process')
#     # hang up parent process, child process become zombie. after then continue
#     result = os.waitpid(-1, 0)
#     print(result)
# else:
#     print('child process')
#     time.sleep(10)
#     exit()
#
# time.sleep(5)
# print('done')

import os
import time

print('loading')
retval = os.fork()
if retval:
    print('parent process')
    result = os.waitpid(-1,1)  # don't hang up parent process
    print(result)
else:
    print('child process')
    time.sleep(10)
    exit()

time.sleep(20)
print('done')