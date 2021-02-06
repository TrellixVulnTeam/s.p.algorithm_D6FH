# Factorial(N) = N * Factorial(N-1)
# ...
# Factorial(1) = 1
#재귀
def factorial(n):                          # 02 06 10 14
    if n == 1:# 탈출조건  Factorial(1) = 1   # 03 07 11 15
        return 1           #                           16

    return n * factorial(n-1)   # 04 08 12


print(factorial(5))                        # 01 05 09 13 17

                                #5*4*3*2*1 = 120