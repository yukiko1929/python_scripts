# a = 12 ** 3
# b = 6 ** 3
#
# print(a)
# # print(b)
for a in range(1,101):
    for b in range (1,101):
        for c in range(1,101):
            for d in range(1,101):
                if a ** 3 + b ** 3 + c ** 3 == d ** 3:
                    print(a,b,c,d)

# result = 90 ** 3 + 53** 3 + 19 ** 3
# result2 = 96 **3
# print(result)
# print(result2)
