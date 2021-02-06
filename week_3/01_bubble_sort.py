input = [4, 6, 2, 9, 1]
#5개의 인자 4번 비교 필요
#4개의 인자 3번 비교
#3개의 인자 2번 비교
#2개의 인자 1번 비교



def bubble_sort(array):#버블 정렬
    n = len(array) #O(N^2) 의 시간 복잡도
    for i in range(n - 1):
        for j in range(n - i - 1):  # n = 5 이면 0123 012 012 01 0
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]# 순서를 바꿈
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!