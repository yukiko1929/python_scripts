import re

class countings:
    def many_counts(self,filename,patterns):
        count_dict = {}
        cpattern = re.compile(patterns)

        with open(filename) as fobj:
            for line in fobj:
                m = cpattern.search(line)
                if m:
                    key = m.group()
                    count_dict[key] = count_dict.get(key, 0) + 1
        return count_dict

if __name__ == '__main__':
    c = countings()
    ip = '(\d\.){3}\d+'
    print(c.many_counts('/mnt/access_log', ip))