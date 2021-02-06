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
def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = 0
    head_1 = linked_list_1.head
    while head_1 is not None:# head_1에 head_1.next를 넣으면서 노드가 사라질때까지 이동
        sum_1 = sum_1 * 10 + head_1.data# head_1의 데이터값을 더함
        #6 -> 67 -> 678
        head_1 = head_1.next

    sum_2 = 0
    head_2 = linked_list_2.head
    while head_2 is not None:  # head_1에 head_1.next를 넣으면서 노드가 사라질때까지 반복
        sum_2 = sum_2 * 10 + head_2.data  # head_1의 데이터값을 더함
        # 3 -> 5 -> 4
        head_2 = head_2.next
    print(sum_1)
    print(sum_2)

    return sum_1 + sum_2


  # head
#   [6] -> [7] -> [8]
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)
  # head
#   [3] -> [5] ->[4]
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
