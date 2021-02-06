class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

   #head -> next -> next -> next -> None 링크드 리스트 끝으로 가려면 순차적으로 진해되어야함
   # 첫번째 방법 LinkedList 길이 전부 알아낸 후 그 길이에서 k만큼 뺀 길이만큼 이동
    def get_kth_node_from_last(self, k):
        length = 1 # 길이를 재기 위한 정수 초기화 1을 두는 이유 처음 헤드노드 있기때문에 0이 아닌 1이라 설정
        cur = self.head #노드를 이동하기 위한 새로운 변수 cur 에다가 head를 담는다.

        while cur.next is not None:
            cur = cur.next
            length += 1
        end_length = length - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next

        return cur

    #두번째방법 두개의 포인터 이용 노드를 2개 잡는다.
    #       1 2 3 4 5 6 7 8 ... 끝 예를들어 k = 6
    #  시작:ㅁ<-간격 6--->ㅁ
    #  진행:  ㅁ<-간격 6--->ㅁ 한칸씩 계속 이동
    #  끝나면:           ㅁ<-간격 6--->ㅁ 앞에있는 노드가 끝에 도달했을때 뒤에노드는 6만큼 떨어진 곳이 있다.
    def get_kth_node_from_last(self, k):
        slownode = self.head # 늦은 노드
        fastnode = self.head # 빠른 노드

        for i in range(k):
            fastnode = fastnode.next

        while fastnode is not None:
            fastnode = fastnode.next
            slownode = slownode.next
        return slownode
# 시간복잡도는 방법 1, 2 가 같음
linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)



print(linked_list.get_kth_node_from_last(2).data) # 7이 나와야 합니다!