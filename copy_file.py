# #copy file script
#
# original_file = open('/bin/ls','rb')
# data = original_file.read()
#
# new_file = open('/root/new','wb')
# new_file.write(data)
# new_file.flush()
# new_file.close()
#
# original_file.close()
#
# #to improve the script above

ori_file = input('old file path:')
new_file = input('new file path:')

ori_fobj = open(ori_file,'rb')
new_fobj = open(new_file,'wb')

while True:
    data = ori_fobj.read(4096)
    if data == b'':              # if there is no more data to read, then break. otherwise, continue to write.
    # if len(data) == 0:
    # if not data:
        break
    new_fobj.write(data)

ori_fobj.close()
new_fobj.close()

# to use position variables
import sys
lists = print(sys.argv)

old_file = lists[1]
new_file = lists[2]

print(old_file)

