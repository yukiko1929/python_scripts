import os

# def score():
#     # score_dict = {}
#     # alist = [20170123, 61, 20170233, 97, 20170124, 100, 20170243, 98, 20180072, 56]
#     # length = len(alist)
#     # for ind,value in enumerate(alist):
#     #     for th in range(length - 1):
#     #     # print(ind)
#     #     # print(value)
#     #         score_dict[ind, lambda x: x %2 == 0] = alist[','.join(th,lambda x : x % 2 == 1)]
#     # return score_dict
#     score_dict = {}
#     alist = [20170123, 61, 20170233, 97, 20170124, 100, 20170243, 98, 20180072, 56]
#     # score_dict[alist[-1]] = alist[-2]
#     # print(score_dict)
#     length = len(alist)
#     for i in range(length - 1):
#         if i % 2 == 0:
#             score_dict[alist[i]] = alist[i + 1]
#     return score_dict
#
# if __name__ == '__main__':
#     score()

def score():
    alist = [20170123, 61, 20170233, 97, 20170124, 100, 20170243, 98, 20180072, 56]
    score_dict = {}
    length = len(alist)
    for i in range(length - 1):
        if i % 2 == 0:
            #print(alist[i])
            score_dict[alist[i]] = alist[i + 1]
    return score_dict

if __name__ == '__main__':
    score()
    print(score())