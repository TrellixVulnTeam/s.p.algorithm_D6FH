class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):# head가 [4] 였는데 [3] -> [4] head를 3으로 바꾸고 4를가르키게 한다.
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    # pop 기능 구현
    def pop(self):# [3] -> [4] head[3]을 없에고 head를 다시 [4]로 잡는다.
        if self.is_empty():#만약 스텍이 비었다면 Stack is Empty 리턴
            return"Stack is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head#삭제된 head 반환

    def peek(self):#head 값을 본다.
        if self.is_empty():#만약 스텍이 비었다면 Stack is Empty 리턴
            return"Stack is Empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):#비었는지 확인
        return self.head is None# None 이라면 비었으므로 True 반환

stack = Stack()# 클래스 Stack 호출
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.peek())