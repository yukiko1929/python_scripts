import sys

def copy(ori_file, new_file):
    ori_fobj = open(ori_file, 'rb')
    new_fobj = open(new_file, 'wb')

    while True:
        data = ori_fobj.read(4096)
        if data == b'':
            # if len(data) == 0:
            # if not data:
            break
        new_fobj.write(data)

    ori_fobj.close()
    new_fobj.close()

copy(sys.argv[1],sys.argv[2])