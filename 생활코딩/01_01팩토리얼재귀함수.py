# #n! = 1 * 2 * 3 * ...(n-2) * (n-1)*n
# def factorial_1(n):
#     변수 = 1
#     for i in range(1, n + 1):
#         변수 *= i
#     return 변수
#
# # 0! = 1
# # n! = n * (n-1)!
#
# def factorial_2(n):#재귀
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_2(n - 1)#재귀함수
#
# print(factorial_1(10))
# print(factorial_2(10))


#피보나치수열 재귀함수의 문제점
counter = 0 #피보나치 20을계산했을때 계산이 몇번일어나는지 확인용
def f(n):
    global counter #파이썬은 함수밖의 인자를 global을 통해 가져온다 (),[],{} 초기화 제외
    counter += 1
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)
print(f(5))
print(counter)

#메모화(memoization) 피보나치재귀 보완하는 기술 한번계산했던 것은 메모에서 확인하는식
counter = 0
메모 = { 1: 1, 2: 1 }
def f(n):
    global counter
    counter += 1
    if n in 메모:
        return 메모[n]
    else:
        output = f(n-1) + f(n-2)
        메모[n] = output
        return output
print(f(20))
print(counter)

#조기리턴 (들여쓰기 단계를 줄인다)
counter = 0
메모 = { 1: 1, 2: 1 }
def f(n):
    global counter
    counter += 1
    if n in 메모:
        return 메모[n]

    output = f(n-1) + f(n-2)
    메모[n] = output
    return output
print(f(20))
print(counter)