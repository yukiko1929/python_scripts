import os

class Convert:

    def __init__(self, filename):
        self.filename = filename

    def to_linux(self):
        defile = os.path.splitext(self.filename)[0] + '.linux'
        with open(self.filename, 'r') as sobj:
            with open(defile, 'w') as dobj:
                for line in sobj:
                    line = line.rstrip() + '\n'
                    dobj.write(line)

    def to_windows(self):
        defile = os.path.splitext(self.filename)[0] + '.windows'
        with open(self.filename, 'r') as sobj:
            with open(defile, 'w') as dobj:
                for line in sobj:
                    line = line.rstrip() + '\r\n'
                    dobj.write(line)

if __name__ == '__main__':
    c = Convert('/mnt/yuki.txt')
    c.to_linux()
    c.to_windows()