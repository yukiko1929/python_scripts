import re
from collections import Counter

# def log_analysis(filename, patterns):
#     # result_list = []
#     # cpa = re.compile(patterns)
#     # with open(filename) as fobj:
#     #     for lines in fobj:
#     #         match = cpa.search(lines)
#     #         if match:
#     #             mag = match.group()
#     #             result_list.append(mag)
#     #
#     # return result_list
#
#     result_dict = {}
#     cpa = re.compile(patterns)
#     with open(filename) as fobj:
#         for lines in fobj:
#             match = cpa.search(lines)
#             if match:
#                 mag = match.group()
#                 result_dict[mag] = result_dict.get(mag, 0) + 1
#     return result_dict
#
#
#
#
# if __name__ == '__main__':
#     filena = '/mnt/access_log'
#     patterns = '(\d\.){3}\d+'
#     result = log_analysis(filena, patterns)
#     print(result)

class LogAna:
    def __init__(self, filename):
        self.filename = filename

    def analysis(self, patterns):
        result_dict = {}
        # result = Counter()
        cpa = re.compile(patterns)
        with open(self.filename) as fobj:
            for lines in fobj:
                match = cpa.search(lines)
                if match:
                    mag = match.group()
        #             result.update([mag])
        # return result
                    result_dict[mag] = result_dict.get(mag, 0) + 1
        return result_dict

class AmouCon:
    def __init__(self, filename):
        self.filename = filename

    def counting(self, patterns):
        result = Counter()
        cpa = re.compile(patterns)
        with open(self.filename) as fobj:






