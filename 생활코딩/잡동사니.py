# scores = {"철수": 90, "민수": 85, "영희": 80}
#
# items = scores.items()
# print(items)


# d1 = {'a':1, 'b':2}
# d2 = {'c':1, 'd':2}
#
# d1.update(d2)
# d1['d'] = 4
# print(len(d1))
# print(d1['d'])
# print(d1.keys())


n = int(input())
dic = {}
for i in range(1, n+1):
    제품명 = input('')
    수량 = int(input())
    dic[제품명] = 수량
# print(dic)
sortedlist = sorted(dic.items(), key = lambda x: x[0])# , reverse = True)

# print(sortedlist)
result_list = []

max_num = sortedlist[0][1]
for j in sortedlist:
    # print(j[1])
    if j[1] > max_num:
        max_num = j[1]

for k in sortedlist:
    if k[1] == max_num:
        result_list.append(k)
print(result_list[0][0])








# print(list)



# N = int(input())
# P = int(input())
# 주기 = 0
# 집합_list = []
#
# for i in range(N):
#     원소 = 0
#     주기 = int(input())
#
#     for j in range(0, P+1):
#         원소 += 주기
#         집합_list.append(원소)
#         if max(집합_list) > P:
#             집합_list.remove(원소)
#
# # print(집합_list)
# # print(set(집합_list))
# print(len(set(집합_list)))

# 딕셔너리 = {"문자열": "값", 273: [1, 2, 3, 4], True: False}
#
# print(딕셔너리)
#
# for key in 딕셔너리:
#     print("{}:{}".format(key, 딕셔너리[key]))
