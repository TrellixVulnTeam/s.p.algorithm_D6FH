s = "(())()"


def is_correct_parenthesis(string):#스텍 이용
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] == ")":# 여는 괄호가 있어야 닫는괄호가 의미가 있어지기 때문
            if len(stack) == 0:
                return False
            else:
                stack.pop()#열고 닫힌 괄호는 사라진다.

    if len(stack) == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!