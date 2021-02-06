# 회문 ex) '토마토' 'abcba' ...

input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]: # 배열 인덱스 문자열 대칭, 앞뒤 판별
            return False

    return True

print(is_palindrome(input))

