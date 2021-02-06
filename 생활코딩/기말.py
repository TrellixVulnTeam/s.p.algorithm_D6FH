
N = int(input())

a = []
b = []
for i in range(1, N + 1):
    a.append(i)
    # print(a)
    while (i != 0):
        b.append(i % 10)
        i = i // 10

# print(b)
c = []
for j in b:
    if j % 3 == 0:
        c.append(j)
    if j == 0:
        c.remove(j)

print(b)
print(c)
print(len(c))
#---------------------------------------
# A = [[1,"AA"], [2,"CC"], [1,"DD"]]
# a = []
# 정수 = int(input())
# 문자열 = str(input())
# a.append(정수)
# a.append((문자열))
# A.append(a)
# A.sort()
# print(A)
#----------------------------
# 입력 = str(input())
# 추가 = str(input())
# A = []
# B = []
# C = []
# A.append(입력)
# if
# B.append(추가)
# C = A + B
#
# print(C)
# sum = "".join(C)
# print(sum)


# 정수 = int(input())
# 문자열 = str(input())
#----------------------------------
# dic = {}
# while True:
#     t = input()
#     if(t == "-1"):
#         break
#     if(len(t) > 1):
#         u = t[-1:-3:-1]
#         if((u in dic) == False):
#             dic[u] = 1
#         else:
#             dic[u]=dic[u]+1
# print(dic)

