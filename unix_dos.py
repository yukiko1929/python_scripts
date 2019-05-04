# class convert:
#     def __init__(self, srcf, dstf):
#         self.srcf = srcf
#         self.dstf = dstf
#
#     def unix_to_dos(src, dest):
#         with open(src, 'r') as sobj:
#             with open(dest, 'w') as dobj:
#                 for line in sobj:
#                     line = line.rstrip() + '\n'
#                     dobj.write(line)
#
#     def dos_to_linux(src, dest):
#         with open(src, 'r') as sobj:
#             with open(dest, 'w') as dobj:
#                 for line in sobj:
#                     line = line.rstrip() + '\r\n'
#                     dobj.write(line)
#
# if __name__ == '__main__':
#     convert.dos_to_linux('/mnt/passwd', '/mnt/passwd.linux')
#     convert.unix_to_dos('/mnt/passwd','/mnt/passwd.windows')

import os

class Convert:
    def __init__(self, file):
        self.file = file

    def to_windows(self):
        destfile = os.path.splitext(self.file)[0] + '.windows'
        with open(self.file, 'r') as srobj:
            with open(destfile, 'w') as dobj:
                for line in srobj:
                    line = line.rstrip() + '\r\n'
                    dobj.write(line)

    def to_linux(self):
        destfile = str(os.path.splitext(self.file))[0] + '.linux'
        # mid_file = os.path.basename(self.file)
        # destfile = mid_file.split('.') + '.linux'
        with open(self.file, 'r') as srobj:
            with open(destfile, 'w') as dobj:
                for line in srobj:
                    line = line.rstrip() + '\n'
                    dobj.write(line)

if __name__ == '__main__':
    Convert.to_linux('/mnt/yuki.txt')
    Convert.to_windows('/mnt/yuk.txt')