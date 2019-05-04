import os
import pickle
import tarfile
import hashlib
from time import strftime

def check_md5(file):
    m = hashlib()
    with open(file, 'rb') as fobj:
        while True:
            data = fobj.read(1024)
            if not data:
                break
            else:
                m.update(data)
    return m.hexdigest()

def full_back(src, dest, md5file):
    fname = os.path.basename(src)
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)

    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    md5dict = {}
    for path, dire, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


def incre_back(src, dest, md5file):
    fname = os.path.basename(src)
    fname = '%s_incre_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)

    md5dict = {}
    for path, dire, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if md5dict[key] != old_md5.get(key):
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    src = '/tmp/mydemo/security'
    dest = '/tmp/demo'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') == 'Mon':
        full_back(src, dest, md5file)
    else:
        incre_back(src, dest, md5file)

