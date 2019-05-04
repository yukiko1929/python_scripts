from random import randint, choice
from string import ascii_letters, digits

first_char = ascii_letters + digits

# def func1(x):
#     return x % 2
#
# if __name__ == '__main__':
#     nums = [randint(1,100) for i in range(11)]
#     print(nums)
#     resule = filter(func1, nums)
#     print(list(resule))

def func2(x):
    return x ** 2

nums = [randint(1,50) for i in range(10)]
print(nums)
result = filter(lambda x: x % 2, nums)
print(list(result))

result2 = map(func2, nums)
print(list(result2))

print('#' * 50)
result3 = map(lambda x: x ** 2, nums)
print(list(result3))
print('#' * 50)
nums2 = [nums ** 2 for i in nums]    # 列表解析不熟练
print(nums2)

# my_char = [choice(first_char) for i in range(10)]
# print(my_char)
# result = filter(lambda x: x in digits, my_char)
# print(list(result))

