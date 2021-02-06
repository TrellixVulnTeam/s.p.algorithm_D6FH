input = 'tolot'
#문자열 슬라이싱과 재귀함수 이용

# is_palindrome(string) = 맨앞뒤 검사를 했다면 is_palindrome(string[1:-1]) 로 축소를 할 수 있다.
def is_palindrome(string):
    if string[0] != string[-1]: # 탈출조건 맨앞과 맨뒤가 다르다면 False
        return False
    if len(string) <= 1:
        return True

    return is_palindrome(string[1:-1])# 마치 팩토리얼 재귀처럼 문자열 슬라이싱 맨앞 맨뒤 빼면서 len(string) 값이 1이 될때까지 반복

print(is_palindrome(input))