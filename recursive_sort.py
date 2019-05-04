from random import randint

def sorting(seq):
    choice = input('asc or desc:')
    if choice == 'asc':
        if len(seq) < 2:
            return seq
        else:
            middle = seq[0]
            smaller = []
            larger = []
            for i in seq[1:]:
                if i < middle:
                    smaller.append(i)
                else:
                    larger.append(i)
                    return sorting(smaller) + [middle] + sorting(larger)
    return sorting(larger) + [middle] + sorting(smaller)


def odd_or_even(nums):
    nums = sorting(nums)
    choice = input('even or odd:')
    if choice not in ['odd', 'even']:
        print('invalid input')
    elif choice == 'odd':
        return filter(lambda x:x % 2 ==1, nums)
        # odd = sorting(odd_original)
    # else:
    #     even_original = filter(lambda x:x % 2 == 0, nums)
    #     #even = sorting(even_original)
    return  filter(lambda x:x % 2 ==1, nums)





if __name__ == '__main__':
    numbers = [randint(1,100) for i in range(20)]
    # odds = filter(lambda x:x % 2 == 1, nums)
    # even = filter(lambda x:x % 2 == 0, nums)
    # print(nums)
    # print(sorting(nums))
    print(numbers)
    odd_or_even(numbers)
