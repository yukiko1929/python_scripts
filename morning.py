# for i in range(1,10):
#     for j in range(1, i+1):
#         print('%s * %s = %s' % (i, j, i*j), end = ' ')
#     print()

# file object
ori_obj = open('/tmp/passwd','rb')
new_obj = open('/opt/passwd','wb')

data = ori_obj.read()
new_obj.write(data)

ori_obj.close()
new_obj.close()

# # to use function in cpoy script
# import sys
# def copy(src_file,dest_file):
#     data = src_file.read()
#     dest_file.write(data)
#
#     src_file.close()
#     dest_file.close()
#
# copy(sys.argv[1],sys.argv[2])
import sys
def copy(sour,destina):
    with open(sour,'rb') as src_file:
        with open(destina,'wb') as dest_file:
            while True:
                data = src_file.read(4096)
                if not data:
                    break
                dest_file.write()

copy(sys.argv[1],sys.argv[2])


