import os
from sys import argv

# def get_path(dir):
#     for path, folders, files in os.walk(dir):
#         for file in files:
#             pathes = os.path.join(path, file)
#         return pathes
#
# if __name__ == '__main__':
#     result = get_path()
#     print(result)

# def get_path(dir):
#     pathes = os.listdir(dir)
#     for path in pathes:
#         path = os.path.join(pathes, path)
#         print(path)


import os

def all_path(dirname):

    result = []

    for mdir, subdir, file_name_list in os.walk(dirname):

        # print("1:",mdir)
        # print("2:",subdir)
        # print("3:",file_name_list)

        for filename in file_name_list:
            apath = os.path.join(mdir, filename)#合并成一个完整路径
            result.append(apath)

    return result

if __name__ == '__main__':
    result = all_path('/tmp/extract')
    print(result)