input = [4, 6, 2, 9, 1]

# for i in range(5 - 1):      [4, 6, 2, 9, 1]
#                              -  -  -  -  -
#     for j in range(5 - i):  [1, 6, 2, 9, 4]
#                                 -  -  -  -
#         print(i + j)        [1, 2, 6, 9, 4]
#                                    -  -  -
#                             [1, 2, 4, 9, 6]
def selection_sort(array):    #         -  -  선택정렬 : 가장 낮은 값부터 정렬
    n = len(array)

    for i in range(n - 1):  # 시간복잡도 O(N^2)
        min_index = i
        for j in range(n - i):# 하나씩 줄어드므로
            if array[i + j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]



selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!