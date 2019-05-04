import os
import sys
import time

def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result

# if __name__ == '__main__':
#     listall = all_path(sys.argv[1])
#     print(listall)

start = time.time()
result = all_path(sys.argv[1])
end = time.time()
print(all_path(sys.argv[1]))
print(end - start)
print(len(result))