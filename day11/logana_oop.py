import re
import pickle

class LogAnalyse:
    def __init__(self,filename):
        self.filename = filename

    def log(self, pattern):
        calculate = {}
        cpattern = re.compile(pattern)
        with open(self.filename, 'r') as fobj:
            for line in fobj:
                m = cpattern.search(line)
                if m:
                    key = m.group()
                    calculate[key] = calculate.get(key, 0) + 1
        return calculate


    # def log_analysis(self,pattern):
    #     calculate = {}
    #     cpatten = re.compile(pattern)
    #     with open(self,'r') as fobj:
    #         # data = pickle.load(fobj)
    #         for line in fobj:
    #             m = cpatten.search(line)
    #             if m:
    #                 key = m.group()
    #                 calculate[key] = calculate.get(key, 0) + 1
    #     return calculate

if __name__ == '__main__':
    c = LogAnalyse('/mnt/access_log')
    ip = '(\d\.){3}\d+'
    br = 'Firefox|Chrome|MISE'
    result1 = c.log(ip)
    result2 = c.log(br)
    print(result1)
    print(result2)
    # print(log_analysis(file, ip))
    # print(log_analysis(file, br))