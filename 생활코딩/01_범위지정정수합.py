def sum_all(start, end):
    변수 = 0
    for i in range(start, end + 1):
        변수 += i
    return 변수

print(sum_all(1, 100))
print(sum_all(50, 100))
