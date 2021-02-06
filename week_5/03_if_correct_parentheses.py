from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parentheses(string): # 올바른 괄호인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def separate_to_u_v(string): # u, v로 분리
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue: # 큐사용
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right: # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 합니다. 즉, 여기서 괄 쌍이 더 생기면 안됩니다.
            break

    v = ''.join(list(queue))
    return u, v

def reverse_parentheses(string): # 뒤집기
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string

def change_to_correct_parentheses(string):
    if string == '': # 1번
        return ''
    u, v = separate_to_u_v(string) # 2번
    if is_correct_parentheses(u): # 3번
        return u + change_to_correct_parentheses(v)
    else: # 4번
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])

def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string)) # "()(())()"가 반환 되어야 합니다!

# from collections import deque
#
# balanced_parentheses_string = "()))((()"
#
# def is_correct_parentheses(string):
#     stack = []
#     for s in string:
#         if s == '(':
#             stack.append(s)
#         elif stack:# 스텍이 존재할때만 팝한다
#             stack.pop()
#     return len(stack) == 0
#
# def reverse_parenthesis(string):
#     reversed_string = ""  # reversed_string을 "" 로 초기화
#     for char in string[1:-1]:  # string 의 첫번째 에서 마지막을 제거한 상태의 문자열을 돌면서
#         if char == '(':
#             reversed_string += ')'
#         else:
#             reversed_string += '('
#     return reversed_string
#
# def separate_to_u_v(string):
#     reversed_string = ""# reversed_string을 "" 로 초기화
#     for char in string:# u 의 첫번째 에서 마지막을 제거한 상태의 문자열을 돌면서
#         if char == '(':
#             reversed_string += ')'
#         else:
#             reversed_string += '('
# #1. 입력이 빈 문자열인 경우, 빈 문자열 반환
# def change_to_correct_parentheses(string):
#     if string == "":
#         return ""
#     #2. 문자열 w를 두 "균형잡힌 괄호 문자열" u,v 로 분리한다.
#     #단 , u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
#     #v는 빈 문자열이 될 수 있다.
#     # '(' 여는 소괄호 ')'닫는 소괄호 괄호 개수가 같아야한다.
#     u, v = sparate_to_u_v(string)
#
#     #3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해
#     #1단계부터 다시 수행한다. 즉 위에 def is_correct_parentheses(string) 실행
#     # 3-1 에서 수행한 결과 문자열을 u에 이어붙인뒤 반환
#     # -> change_to_correct_parenthesis
#     if is_correct_parentheses(u):
#         return u + change_to_correct_parentheses(v)
#     #4. 문자열 u가 올바른 괄호 문자열이 아니라면 아래 과정을 수행한다.
#     #4-1. 빈 문자열에 첫 번째 문자로 ( 를 붙인다.
#     #4-2 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어붙인다.
#     #4-3 ) 를 다시 붙인다.
#     #4-4. u의 첫번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호방향을 뒤집어서 뒤에 붙인다.
#     else:
#
#         # reversed_string = ""# reversed_string을 "" 로 초기화
#         # for char in u[1:-1]:# u 의 첫번째 에서 마지막을 제거한 상태의 문자열을 돌면서
#         #     if char == '(':
#         #         reversed_string += ')'
#         #     else:
#         #         reversed_string += '('
#         return"(" + change_to_correct_parentheses(v) + ")" + reversed_parenthesis(u[1:-1])
#     queue = deque(string)# 문자열은 큐에다 담는다.
#     left, right = 0, 0 #왼쪽과 오른쪽을 0 으로 초기화
#     u, v = "", "" # u, v를 빈상태로 초기화
#     while queue:# 문자열이 끝날때 까지 큐 왼쪽을 뺀다
#         char = queue.popleft()
#         if char == '(':
#             left += 1
#         else:
#             right += 1
#         if left == right:# 처음 '(' 왼괄호 와 ')' 오른괄호가 같을때 break를 해서 멈춰야함
#             break
#     v = ''.join(list(queue))#  join 앞에 빈칸 ''를 넣고 문자열 리스트를 다 합쳐줌
#     print(u, v)
#     return u, v
# def get_correct_parentheses(balanced_parentheses_string):#올바른 괄호문자열인지 확인
#     if is_correct_parentheses(balanced_parentheses_string):
#         return balanced_parentheses_string
#     else:
#         return change_to_correct_parentheses(balanced_parentheses_string)
#
#
# print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!