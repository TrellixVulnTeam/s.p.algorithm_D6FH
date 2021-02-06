current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# 1. 현재 위치를 청소한다.               r   c           북  동  남  서
# bfs 를 구현 visited = [1, 2, 3]  북 -1   0     dr = [-1, 0, 1, 0]
# 0은 청소하지 않은 장소             동  0   1      dc = [0, 1, 0 ,-1]
# 1은 청소하지 못하는 장소            남  1   0      북 0 동 1 남 2 서 3
# 2는 청소한 장소 라고 표현           서  0  -1      북 왼쪽 회전? 서 0 -> 3
                                             #   동 왼쪽 회전? 북 1 -> 0   규칙성
                                             #   남 왼쪽 회전? 동 2 -> 1   +3 한 후 %4
                                             #   서 왼쪽 회전? 남 3 -> 2
                                             # def get_d_index_when_rotate_to_left(d):
                                             #     return(d + 3) % 4  회전은 인덱스로
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색을 진행
# -> 배열내에서 방향

#a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
# 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.

# b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고
# 2 번으로 돌아간다. -> 현재 본 방향에서 청소할 곳이 없다면 다시 왼쪽으로 회전하라는 의미

# c. 네 방향 모두 청소가 되어있거나 벽인 경우에는 바라보는 방향을 유지한 채로 한 칸 후진하고 2번으로 돌아간다.
# -> 모든 방향이 청소되어있다면 뒤로 한 칸 후진하면 된다.
#   북 뒤 돌기? 남 0 ->2   규칙성
#   동 뒤 돌기? 서 1 -> 3   +2 한 후 %4
#   서 뒤 돌기? 동 3 -> 1
# def get_d_index_when_go_back(d):
#     return(d + 2) % 4

# d. 네 방향 모두 청소가 이미 되어있거나 벽이면서,
# 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_d_index_when_rotate_to_left(d):#방향전환
    return (d + 3) % 4

def get_d_index_when_go_back(d):# 후진
    return (d + 2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_departments_cleaned = 1 #맨처음칸 청소했다고 쳐서 1 로 초기화
    room_map[r][c] = 2#청소를 하면 룸맵 2 로 업데이트
    queue = list([[r, c, d]])

    while queue:#queue가 끝날때 까지 반복
        r, c, d = queue.pop(0)# 맨앞 원소를 뺀다.
        temp_d = d# 방향을 돌리기 위한 임시변수

        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            if 0 <= new_r < n and 0 <= new_c < m and current_room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])#위치와 방향정보 저장
                break

            # c. 네 방향 모두 청소가 되어있거나 벽인 경우에는 바라보는 방향을 유지한 채로 한 칸 후진하고 2번으로 돌아간다.
            # -> 모든 방향이 청소되어있다면 뒤로 한 칸 후진하면 된다.
            elif i == 3:
                new_r, new_c = r + dr[get_d_index_when_go_back(d)], c + dc[get_d_index_when_go_back(d)]
                queue.append([new_r, new_c, temp_d])
                if current_room_map[new_r][ new_c] == 1:
                # d. 네 방향 모두 청소가 이미 되어있거나 벽이면서,
                # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
                    return count_of_departments_cleaned

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))