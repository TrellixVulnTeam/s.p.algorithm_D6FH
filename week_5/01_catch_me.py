from collections import deque

c = 11
b = 2

#코니의 위치 변화
#코니는 처음위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1만큼 움직인다.
#즉 증가하는 속도가 1초마다 1씩 증가한다.

#브라운의 위치 변화는
# B - 1, B + 1, 2 * B
#모든 경우의 수를 나열, BFS적용
#잡았다 라는 의미는 똑같은 시간에 똑같은 위치에 존재해야함

def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))#위치와 시간을 동시에 담아준다.
    visited = [{} for _ in range(200001)]#visited의 각 원소들은 각 시간 0초에 어느 곳을 갔는지를 저장하기 위한 공간
    #visied[위치][시간]
    #visited[3] 에 5라는 키가 있냐? 3위치에 5초에 간적이 있냐?
    while cony_loc <= 200000:
        cony_loc += time # 시간만큼 +1 +2 +3 +4
        if time in visited[cony_loc]:# 브라운의 위치와 시간을 visited 리스트 딕셔너리의에 담고 코니의 시간과 위치는 time으로 동일 하기때문에
            return time#               if time in visited[cony_loc] 이란 조건문을 사용하여 시간을 반환한다.

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_position = current_position - 1
            new_time = current_time + 1

            if 0 <=new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True# 키의 값을 설정한다는 True 다른걸 놔도 상관없음
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <=new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <=new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))


        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!