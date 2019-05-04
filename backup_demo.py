import tarfile
import pickle
from time import strftime
import os
from pathes import all_path
from check_sum import check_md5
from sys import argv

def full_back(src, dest, md5file):
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dest, os.path.basename(src))

    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    md5dict = {}
    for path, folder, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict)


def incre_back(src, dest, md5file):
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dest, os.path.basename(src))

    new_md5dict = {}
    for path, folder, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            new_md5dict[key] = check_md5(key)

    with open(md5file, 'rb') as fobj:
        old_data = pickle.load(fobj)

    with open(md5file, 'wb') as fobj:
        pickle.dump(new_md5dict)

    tar = tarfile.open(fname, 'wb')
    for key in new_md5dict:
        if old_data.get[key] != new_md5dict[key]:
            tar.add(key)
            tar.close()

if __name__ == '__main__':
    choice = '''0:full back
1: incremental backup
2: quit
please enter(0/1/2):'''

    while True:
        sentaku = int(input(choice))
        if sentaku == 0:
            full_back(argv[1], argv[2], argv[3])
            break
        elif sentaku == 1:
            incre_back(argv[1], argv[2], argv[3])
            break
        else:
            print('\nbye-bye')
            break
