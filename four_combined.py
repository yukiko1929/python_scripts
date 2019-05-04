import random

def to_odd(nums):
    # after = filter(lambda x: x % 2 == 1, nums)
    # return after
    for items in nums:
        odd_list = []
        if items % 2 == 1:
            odd_list.append(items)
    return odd_list

def to_even(nums):
    # after  = filter(lambda x: x % 2 == 0, nums)
    # return after
    for items in nums:
        even_list = []
        if items % 2 == 0:
            even_list.append(items)
    return even_list

def asc(seq):
    if len(seq) < 2:
        return seq
    else:
        middle = seq[0]
        smaller = []
        larger = []
        for numbers in seq:
            if numbers < middle:
                smaller.append(numbers)
            else:
                larger.append(numbers)
        return asc(smaller) + [middle] + asc(larger)

def desc(seq):
    if len(seq) < 2:
        return seq
    else:
        middle = seq[0]
        smaller = []
        larger = []
        for numbers in seq:
            if numbers < middle:
                smaller.append(numbers)
            else:
                larger.append(numbers)
        return desc(larger) + [middle] + desc(smaller)

def decide_which(nums):
    choice = '''0:even, desc
1:even, asc
2:odd, desc
3:odd, asc:
please choose(0/1/2/3):'''
    sentaku = int(input(choice))
    if sentaku == 0:
        before = to_even(nums)
        result =  desc(before)
        print(result)
    elif sentaku == 1:
        before = to_even(nums)
        return asc(before)
    elif sentaku == 2:
        before = to_odd(nums)
        return desc(before)
    else:
        before = to_odd(nums)
        return asc(before)

if __name__ == '__main__':
    nums = [random.randint(1,100) for i in range(20)]
    final = decide_which(nums)
    print(final)