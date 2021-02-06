#[3]->[4]
#data, next
class Node:
    def __init__(self, data): #데이터라는 것을 입력받아서 self.data에 저장을 하기 위해 파라미터 data 를 넣는다.
        self.data = data
        self.next = None#처음생성 데이터는 가르키는게 없다.
node = Node(3)
first_node = Node(4)
node.next = first_node
print(node.next.data)# node 3  node.next [4]의 주솟값을 가르킴  node.next.data 4

print(node.data)

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self,data):#head 노드밖에 없는 상태에서 노드가 끝날때 까지 이동을 하여야함
        cur = self.head #cur를 헤드노드라고 지정
        while cur.next is not None: # cur.next == None 일때 까지 반복 링크드 리스트 마지막은 None 이므로
            cur = cur.next #다음 노드로 순차적으로 이동
        cur.next = Node(data)

    # cur = self.head
    #     cur = cur.next  cur를 순차적으로 옮기는데 데이터가 None 일 때 까지
    # while cur.next == None: 구문 실행
    # head
    #  [3] -> [4] -> [5] -> [6] ->[new]
    def print_all(self):
        print("hihihi")
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
linked_list = LinkedList(3)

linked_list.append(4)
linked_list.append(5)
linked_list.print_all()#링크드 리스트 원소 다 출력
