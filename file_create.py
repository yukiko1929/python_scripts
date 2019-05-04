import os
def get_fname():
    fname = input('please enter file name:')
    while 1:
        if os.path.exists(fname):
            print('File %s already existed' % fname)
        else:
            break

def get_content():
    content_lines = []
    while 1:
        one_line = input('please enter one line(enter "end" as close:)\n')
        if one_line == 'end':
            break
        else:
            content_lines.append(one_line)
    return content_lines

def write(fname, content):
    # file_obj = open(fname,'w')
    # file_obj.writelines(line for line in content)
    # file_obj.close()
    with open(fname,'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    fwrite = write(fname, content)
