class MaxHeap:
    def __init__(self):
        self.items = [None]
    #1. 새노드를 맨 끝에 추가한다.
    #2. 지금 넣은 새노드를 부모와 비교한다. 만약 부모보다 크다면 교체한다.
    #3. 이 과정을 꼭대기까지 반복한다.
    def insert(self, value):# O(log(N))만큼의 시간복잡도를 갖는다.
        self.items.append(value)
        cur_index = len(self.items) - 1# 현재 items의 길이에서 -1을 뺀 가장 마지막에 넣은 노드의 인덱스를 cur_index라 저장

        while cur_index > 1:# 힙의 꼭대기 까지,꼭대기는 cur_index가 1 보다 클 때 까지, cur_index가 1이라면 멈춤
            parent_index = cur_index // 2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break
        return 


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!