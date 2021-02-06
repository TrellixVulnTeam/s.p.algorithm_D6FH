# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
# 1. 시작 노드를 스택에 넣는다.
# 2. 현재 스택의 노드를 빼서 visited에 추가한다.
# 3. 현재 방문한 노드와 인접한 노드 중에서 방문하지 않은 노드를 스택에 추가
# 4. 2.부터  반복한다.
# 5. 스택이 비면 탐색을 종료한다.
# 스택을 이용하면 재귀없이 구현가능 무한정 깊어질때의 에러를 안나게할수있다.
def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []

    while stack:#스택이 비지않을때 까지 반복 알고리즘 4주차pdf참고 현재 스택에서 마지막에 넣은 9를빼서 visited에 넣은 후 9 방문
        current_node = stack.pop()
        visited.append(current_node)# visited는 [1]이 들어간다
        for adjacent_node in adjacent_graph[current_node]:#current_node의 adjacent_graph에 인접한 노드에서 뽑는다.
            # print(adjacent_graph)
            # print(adjacent_graph[current_node])
            # print(adjacent_node)
            if adjacent_node not in visited:#방문하지 않은 노드들이 있으면 스택에 추가한다.
                print(visited)
                stack.append(adjacent_node)
    return visited




print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!