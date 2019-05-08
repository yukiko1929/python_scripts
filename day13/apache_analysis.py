import re

def log_ana(fiile,pattern):
    cp = re.compile(pattern)
    con_dict = {}
    with open(fiile) as fobj:
        for lines in fobj:
            con = cp.search(lines)
            key = con.group()
            if not con:
                break
            con_dict[key] = con_dict.get(key = 0) + 1
    return con_dict


if __name__ == '__main__':
    filename = '/mnt/access_log'
    ip = '(\d\.){3}\d+'
    result = log_ana(filename, ip)
    print(result)
