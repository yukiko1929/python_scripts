import time
import threading
import os
import pickle
from time import strftime

def greeting(n=5):
    print('hello yukiko')
    time.sleep(n)
    print('done')

def backup(src,dest,file):
    fname = os.path.basename(src)
    fname = '%s_fullbk_%s' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dest,fname)




if __name__ == '__main__':
    print('loading')
    t1 = threading.Thread(target=greeting)
    t1.start()
    t1.join()
    t2 = threading.Thread(target=greeting, args=(10,))
    t2.start()
