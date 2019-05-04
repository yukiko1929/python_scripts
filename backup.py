import tarfile
import hashlib
import pickle
from time import strftime
import os
from sys import argv
from pathes import all_path

def check_md5(file):
    m = hashlib.md5()
    with open(file, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

def full_backup(dir):
    # # for file in os.listdir(dir):
    # #     original_dict = {file: check_md5(file)}
    #     with open('/tmp/sum_record.txt', 'wb') as fobj:
    #         pickle.dump(original_dict, fobj)
    pathes  = all_path(dir)
    print(pathes)
    ori_dict = {}
    for file in pathes:
        ori_dict[file] = check_md5(file)
        date = strftime('%Y%m%d')
        with open('/tmp/demo/sumcheck_%s.txt' %  date, 'wb') as fobj:
            pickle.dump(ori_dict, fobj)

    tar = tarfile.open('/tmp/demo/%s_fullback_%s.tar.gz', 'w:gz' % (os.path.basename(pathes),date))
    tar.add(file)
    tar.close()

def incre_backup(dir):
    # for file in os.listdir(dir):
    #     now_dict = {file: check_md5(file)}
    #     with open('/tmp/sum_record.txt', 'rb') as fobj:
    #         origin = pickle.load(fobj)
    #     if now_dict.get(file) != origin.get(file):
    #         date = strftime('%Y-%m-%d')
    #         tar = tarfile.open('/tmp/%s_increback.tar.gz', 'w:gz' % date)
    #         tar.add(file)
    #         tar.close()

# if __name__ == '__main__':
#     full_backup('/tmp/extract')

full_backup('/tmp/extract')
