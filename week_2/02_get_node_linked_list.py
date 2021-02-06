class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #처음 생성된 데이터는 다음 노드를 가르치지 않기 때문에 None
# ex) 3 을 가진 Node 를 만드려면
# node = Node(3) 처음생성이므로 next없이 하나의 노드만 있다.

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):# index번째 노드를 반환하시오
        node = self.head #헤드로부터 시작해서 index 만큼 이동해야하기때문에 헤드 지정
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # def add_node(self, index, value):
    #     return "index 번째 Node 뒤에 value 를 추가하세요!"


linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(0).data)


