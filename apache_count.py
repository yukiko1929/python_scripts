import re
def count_pattern(file, patt):
    patt_dict = {}
    cpatt = re.compile(patt)
    with open(file) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                patt_dict[key] = patt_dict.get(key, 0) + 1
    return patt_dict

if __name__ == '__main__':
    fname = '/mnt/access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'Chrome|Firefox|MSIE'
    print(count_pattern(fname, ip))
    print(count_pattern(fname, br))