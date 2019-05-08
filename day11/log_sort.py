import re
#import pickle
from collections import Counter

class LogSort:
    def __init__(self, filename):
        self.filename = filename

    def log_analysis(self,pattern):
        calculate = {}
        counter = Counter()
        cpatten = re.compile(pattern)
        with open(self.filename,'r') as fobj:
            # data = pickle.load(fobj)
            for line in fobj:
                m = cpatten.search(line)
                if m:
                    key = m.group()
                    calculate[key] = calculate.get(key, 0) + 1
                    counter.update([key])
        return counter

if __name__ == '__main__':
    file = '/mnt/access_log'
    ip = '(\d\.){3}\d+'
    br = 'Firefox|Chrome|MISE'
    c = LogSort(file)
    result = c.log_analysis(ip)
    print(result.most_common(2))
    #print(log_analysis(file, ip))
    #print(log_analysis(file, br))