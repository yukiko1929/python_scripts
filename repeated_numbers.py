
a = input('please enter a number(1-9):')
count = int(input('repeated count:'))
list = [0]
for i in range(1,count + 1):
    list.append(a * i)

int_list = [int(numbers) for numbers in list]
print(sum(int_list))

# for i in int_list:
#     mysum = 0
#     mysum += i
#     print(mysum)
# for numbers in list:
#     trans = int(numbers)
#     print(trans)
#         # for num in trans:
#         #     mysum = 0
#         #     mysum += num
#         #     print(mysum)