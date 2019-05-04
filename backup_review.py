import os
import pickle
import tarfile
from time import strftime
import hashlib

def check_md5(file):
    m = hashlib.md5()
    with open(file, 'rb') as fobj:
        while True:
            data = fobj.read(1024)
            if not data:
                break
            else:
                m.update(data)
    return m.hexdigest()


def full_back(src, dest, recordfile):
    fname = '%s_full_%s' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)

    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    md5_dict = {}
    with open(recordfile,'w') as fobj:
        for path, direc, files in os.walk(src):
            for file in files:
                fpath = os.path.join(path, file)
                md5_dict[fpath] = check_md5(fpath)
    return md5_dict

def incre_back(src, dest, recordfile):
    fname = '%s_incre_%s' % (os.path.basename(src), strftime('%Y%m%d'))
    fname = os.path.join(dest,fname)

    new_dict = {}
    for path, dire, files in os.walk(src):
        for file in files:
            fpath = os.path.join(path,file)
            new_dict[fpath] = check_md5(fpath)

    with open(recordfile, 'r') as fobj:
        old_data = pickle.load(fobj)

    with open(recordfile, 'w') as nobj:
        pickle.dump(new_dict)

    tar = tarfile.open(fname, 'w:gz')
    for key in old_data:
        if new_dict[key] != old_data.get(key):
            tar.add(key)
            tar.close()


    # with open(recordfile, 'r') as fobj:
    #     old_dict = fobj.read()
    #     for key in old_dict:
    #         if old_dict[key] != old_dict.get(key):


if __name__ == '__main__':

src = '/mnt/security'
dest = '/mnt/backup'
record = '/mnt/md5_record.file'
