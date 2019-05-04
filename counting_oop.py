import re
from collections import Counter


class countings:

    def __init__(self, filename):
        self.filename = filename

    def many_counts(self,patterns):
        result = Counter()
        # count_dict = {}
        cpattern = re.compile(patterns)

        with open(self.filename) as fobj:
            for line in fobj:
                m = cpattern.search(line)
                if m:
                    key = m.group()
                    result.update([key])
                   # count_dict[key] = count_dict.get(key, 0) + 1
                    # print(count_dict)
        #             for items in count_dict.keys():
        #                 c= Counter()
        #                 c.update(items)
        #             # c = Counter()
        #             # c.update(key)
        return result

        # with open(self.filename) as fobj:
        #     for line in fobj:
        #         m = cpattern.search(line)
        #         if m:
        #             key = m.group()




if __name__ == '__main__':
    c =  countings('/mnt/access_log')
    ip = '(\d+\.){3}\d+'
    br = 'Chrome|MSIE|Firefox'
    a = c.many_counts(ip)
    print(a)
    print(a.most_common(3))
    #print(c.many_counts(br))