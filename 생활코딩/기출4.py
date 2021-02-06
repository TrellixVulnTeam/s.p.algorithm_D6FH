# a, b, c, d, e = map(int, input().split())
#
# list_1 = [a, b, c, d, e]
#
# list_2 = []
# for i in range(1, 5+1):
#     y = list_1[i-1] ** i
#     list_2.append(y)
#
#
# print(sum(list_2))

def pow(x, y):
    ss = 1
    for i in range(0, y):
        ss = ss * x
    return ss

su = 0
for i in range(1, 5+1):
    t = int(input("Num:"))
    su = su + pow(t, i)
print(su)

