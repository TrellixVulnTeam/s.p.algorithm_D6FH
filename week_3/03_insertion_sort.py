input = [4, 6, 2, 9, 1]
# [4 6 2 9 1] #6부터 시작 뒤에꺼를 앞에꺼랑 비료해서 넣으므로
#  <-
# [2 4 6 9 1]
#  <-<-
# [2 4 6 9 1]
#  <-<-<-
# [1 2 4 6 9]
#  <-<-<-<-

# for i in range(1, 5):    #1 21 321 4321
#     for j in range(i):
#         print(i - j)

def selection_sort(array): #배열이 어느정도 갖춰지면 삽입정렬일 경우 조금 이득을 볼 수 있다.
    n = len(array)
    for i in range(1, n): #마찬가지로 O(N^2) 만큼의 시간 복잡도가 걸리지만
        for j in range(i):# 버블,선택이랑 다른점 밑에 break문
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j -1]
            else:# 왼쪽보다 오른쪽 수가 더 크면 비교하지 않고 break ex)
                break#ex) [2, 4, 6, 9, 1] 정렬이 되다가 9를 6과 비교할때 6에서 조건이 아님 4,2 도 맞지 않으므로 else: break

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!