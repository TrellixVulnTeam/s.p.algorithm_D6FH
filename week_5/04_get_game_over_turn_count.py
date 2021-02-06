k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

#말은 순서대로 이동한다. -> 말의 순서에 따라 반복문
#말이 쌓일 수 있다. -> 맵에 말이 쌓이는 걸 저장해놔야 한다.
#쌓인 순서대로 이동한다 -> stack 써야겠구나

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_count = 1
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]# 3차원 배열의 구성
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]# 로우 칼럼 디렉션을 행렬에서 뽑는다.
        current_stacked_horse_map[r][c].append(i)# i번째의 말이 r,c 위치에 위치해 있다.
       # print(current_stacked_horse_map)


    while turn_count <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:#범위를 벗어나거나 그 칸이 파란색인 경우 반대로 한칸 이동
                new_d = get_d_index_when_go_back(d)

                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]
                #가기로 한곳이 막혀있음 안감
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue# 아무것도 안하고 컨티뉴
            # 2가 이동한다고 치면, 2랑 3만 이동.
            # 즉, 자기자신의 인덱스 보다 큰 애들만 데리고 간다.
            # [1, 2, 3] [:i}
            moving_horse_index_array = []
            for i in range(len(current_stacked_horse_map[r][c])):
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]
                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)# 뒤집어서 넣는다.
            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c
    #턴이 진행되는 중 말이 4개 이상 쌓이는 순간 게임이 종료된다.
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count
        turn_count += 1# while문을 돌 때 마다 하나씩 증가시켜야 원하는 결과를 볼 수 있다.
        print(current_stacked_horse_map)
    return -1# while 1000을 다해도 게임이 끝나지 않으면 -1 반환


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다