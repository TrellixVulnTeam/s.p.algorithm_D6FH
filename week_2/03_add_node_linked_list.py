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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value): #인덱스 번째에 새로운 원소 값(value)을 추가
        new_node = Node(value)
        if index == 0:# index 0 일때 head노드 교체
            new_node.next = self.head# [6] new_node.next를 self.head 로 지정을 해야 [6]다음[5] 가 오는것을 알고나서
            self.head = new_node# [6]->[5]-> ...
            return
        new_node = Node(value)# [6]
        node = self.get_node(index - 1) #위에get_node 함수사용, n번째 추가 이므로 index- 1, 0번째 노드[5] but index 값이 0 이 들어올 경우 예외처리를 해줘야함
        next_node = node.next# [12]   # (index - 1) -1 이 들어가면 항상 index가 0일 때의 예외처리를 생각해야함
        node.next = new_node# [5]->[6] 으로 만듬
        new_node.next = next_node# [6]->[12]


#      index   next_node
#     ['자갈']->['밀가루']->[우편] :밀가루를 빼고 흑연을 놓고싶다.
#              new_node           밀가루칸에 next_node저장
#             ->['흑연']->         흑연에 new.node 저장
# index.next = new_node # index 다음 new_node 지정
# new_node.next = next_node #new_node 다음 next_node 로 지정

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# [5]->[12]->[8]

#[5]->[6]->[12]->[8]
linked_list.add_node(1, 6) # 1번째(index -1)에 [6] 추가
linked_list.print_all()


