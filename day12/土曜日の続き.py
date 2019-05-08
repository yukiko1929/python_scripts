# def score():
#     alist = [20170123, 61, 20170233, 97, 20170124, 100, 20170243, 98, 20180072, 56]
#     score_dict = {}
#     length = len(alist)
#     for i in range(length - 1):
#         if i % 2 == 0:
#             #print(alist[i])
#             score_dict[alist[i]] = alist[i + 1]
#     return score_dict
#
# if __name__ == '__main__':
#     score()

import pickle

def score_sort(scorefile):
    alist = [20190123, 61, 20170233, 97, 20170124, 100, 20170243, 98, 20180072, 56]
    score_dict = {}
    nums = len(alist)
    for i in range(nums - 1):
        if i % 2 == 0:
            score_dict[alist[i]] = alist[i + 1]

    with open(scorefile, 'wb') as fobj:
        pickle.dump(score_dict, fobj)

    stu_id = list(score_dict)
    stu_id.sort(reverse=False)

    new_dict = {}
    with open(scorefile, 'rb') as fobj:
        data = pickle.load(fobj)
        for items in stu_id:
            new_dict[items] = data.get(items)
    return new_dict

    #return score_dict

if __name__ == '__main__':
    scorefile = '/mnt/scorefile.txt'
    result = score_sort(scorefile)
    print(result)