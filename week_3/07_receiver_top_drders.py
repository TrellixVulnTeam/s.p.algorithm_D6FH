
# [0, 0, 2, 2, 4] 답
# [0, 0, 0, 0, 0] 시작으로 리스트 0 초기화

#   <- <- <- <- <-
#   6  9  5  7  4
#  [0, 0, 0, 0, 4]

#   <- <- <- <-
#   6  9  5  7
#  [0, 0, 0, 2, 4]

#   <- <- <-
#   6  9  5
#  [0, 0, 2, 2, 4]
#     .
#     .

top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)# 탑 길이만큼 리스트 0으로 초기화
    while heights:# heights 가 빈상태가 아닐때 까지 반복, O(N) 총 O(N^2)만큼의 시간복잡도
        height = heights.pop()#heights.pop()으로 height를 맨뒤에서 부터 뽑는다. 즉 처음height는 4
        for idx in range(len(heights) - 1, 0 - 1, -1):# 반대로 4 3 2 1 0 반복 가운데 0-1 은 미만의 개념이므로 #O(N)
            if heights[idx] > height:#레이져가 부딪히는조건
                print(answer)#확인용 print
                answer[len(heights)] = idx + 1 # 0 1 2 3 4 인덱스가아닌 1 2 3 4 5 로 표현해야 하므로
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!