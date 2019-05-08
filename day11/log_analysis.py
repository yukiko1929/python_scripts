import re
import pickle

def log_analysis(file,pattern):
    calculate = {}
    cpatten = re.compile(pattern)
    with open(file,'r') as fobj:
        # data = pickle.load(fobj)
        for line in fobj:
            m = cpatten.search(line)
            if m:
                key = m.group()
                calculate[key] = calculate.get(key, 0) + 1
    return calculate

if __name__ == '__main__':
    file = '/mnt/access_log'
    ip = '(\d\.){3}\d+'
    br = 'Firefox|Chrome|MISE'
    print(log_analysis(file, ip))
    print(log_analysis(file, br))






