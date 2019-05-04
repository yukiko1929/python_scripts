# from sys import argv
# #import pickle
# import h

# import hashlib
# from sys import argv
#
# def check_md5(file):
#     with open(file, 'rb') as fobj:
#         data = fobj.read()
#     md5_result = hashlib.md5(data)
#     print(md5_result.hexdigest())
#
# if __name__ == '__main__':
#     check_md5(argv[1])

import hashlib
import sys

def check_md5(file):
    m = hashlib.md5()
    with open(file, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

if __name__ == '__main__':
    try:
        file = sys.argv[1]
    except IndexError:
        print('usage: %s  filename' % sys.argv[0])

    print(check_md5(file))