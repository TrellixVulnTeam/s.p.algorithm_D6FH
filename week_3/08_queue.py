class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# head   tail  [3] 을 [2] 다음에 넣는 과정
# [4] -> [2]
#new_node = Node(3)

# head   tail
# [4] -> [2] -> [3]
#self.tail.next = new_node

# head          tail
# [4] -> [2] -> [3]
#self.tail = new_node

class Queue:
    def __init__(self):# 큐는 선형구조이기 때문에 인과 아웃 head와 tail 지정
        self.head = None
        self.tail = None
# 처음 [3] 이들어오면 초기에 head와 tail이 None으로 같기 때문에 [3]은 head와 tail 이다. 따라서 예외처리 필요
    def enqueue(self, value):
        new_node = Node(value)# enqueue에서 받느 value값을 넣어 new_node 생성
        if self.is_empty():#예외처리
            self.head = new_node
            self.tail =new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    #head          tail
    #[4] -> [2] -> [3]

    #delete_head = self.head
    #self.head = self.head.next
    #return delete_head

    #head   tail
    #[2] -> [3]   [4] 반환
    def dequeue(self):# 헤드정보를 뽑는다
        if self.is_empty():
            return"Queue is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data# 헤드정보(주소).값를 뽑는다.

    def peek(self):# 맨앞에 데이터 보기
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):
        # 어떻게 하면 될까요?
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())
