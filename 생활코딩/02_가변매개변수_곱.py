def mul(*values):
    변수 = 1# 곱샘과 관계없는 '1'
    for i in values:
        변수 *= i
    return 변수
print(mul(5, 7, 9, 10))# 가변매개변수 위에 함수선언부분 '*'