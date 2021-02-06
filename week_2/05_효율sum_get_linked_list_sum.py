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
    sum_1 = 효율_get_linked_list_sum(linked_list_1)
    sum_2 = 효율_get_linked_list_sum(linked_list_2)

    print(sum_1)
    print(sum_2)

    return sum_1 + sum_2


def 효율_get_linked_list_sum(linked_list):# linked_list구조를 반복하고 있기때문에 인자로 linked_list를 인자로 받는다
    linked_list_sum = 0
    head = linked_list.head
    while head is not None:
        linked_list_sum = linked_list_sum * 10 + head.data
        head = head.next
    return linked_list_sum
  # head
# [6] -> [7] -> [8]
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)
  # head
# [3] -> [5] ->[4]
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
