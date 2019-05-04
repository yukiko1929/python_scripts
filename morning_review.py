from time import strftime
import pickle
# from os import path
# from os import listdir
import tarfile
import os

import hashlib

def check_md5(src_file):
    m = hashlib.md5()
    with open(src_file, 'rb') as fobj:
        while True:
            data = fobj.read()
            if not data:
                break
            m.update(data)
    return m.hexdigets()

def full_back(src, dest, recordfile):
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)

    md5dict = {}
    for path, dir, files in src:
        for file in files:
            key = os.path.join(path,file)
            md5dict[key] = check_md5(key)
    with open(recordfile, 'wb') as fobj:
        pickle.dump(fobj, md5dict)

    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

def incre_back(src, dest, recordfile):
    fname = '%s_incre_%s.tar.gz' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)


    new_md5 = {}
    for path, dir, files in src:
        for file in files:
            key = os.path.join(path, file)
            new_md5[key] = check_md5(key)

    with open(recordfile, 'rb') as fobj:
        old_data = pickle.load(fobj)

    tar = tarfile.open(fname, 'w:gz')
    for key in new_md5:
        if old_data.get(key) != new_md5[key]:
            tar.add(key)
    tar.close()

def menu(src, dest, record):
    cmds = {0:full_back, 1: incre_back}
    choice = '''0:full backup
1: incremental backup
please choose:'''
    sentaku = int(input(choice))
    cmds[sentaku](src, dest, record)

if __name__ == '__main__':
    src = '/tmp/demo'
    dest = '/tmp/backup'
    recordfile = '/tmp/md5_record'










