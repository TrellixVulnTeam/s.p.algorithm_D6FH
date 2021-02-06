# N = int(input())
#
# list = []
#
# for i in range(2, N):
#     if N % i == 0:
#         list.append(i)
#         N = N / i
# print(list)
#
# import math
# N = int(input())
# li = []
# while N != 1:
#     for i in range(2, N + 1):
#
#         if(N % i == 0):
#
#
#             N = N//i
#             li.append(i)
#             break
# b = list(set(li))
#
#
# print(b[2]*b[3])

# a = int(input())
# b = int(input())
# c = int(input())
#
# list = []
# list.append(a)
# list.append(b)

# list.append(c)
#
# list.remove(max(list))
# list.remove(min(list))
#
# print(list[0])
#
# n = int(input())



# for i in range(1, n + 1):
#     i = str(i)
#     for j in range(1, n + 1):
#         if j <= int(i):
#             print(i, end='')
#     print('a')

# class Person:
#     def __init__(self):
#         self.name = input('이름:')
#         self.age = int(input('나이:'))
#     def disp(self):
#         print(self.name)
#         print(self.age)
# li = []
# for i in range(10):
#     li.append(Person())
#
# for i in range(len(li)):
#     li[i].disp()

temp1 = [[]] * 3
print("temp1 :", id(temp1))
print("temp1[0] : ", id(temp1[0]))
print("temp1[1] : ", id(temp1[1]))
print("temp1[2] : ", id(temp1[2]))
print("------------------")
temp2 = [[], [], []]
print("temp2 :", id(temp2))
print("temp2[0] :", id(temp2[0]))
print("temp2[1] :", id(temp2[1]))
print("temp2[2] :", id(temp2[2]))