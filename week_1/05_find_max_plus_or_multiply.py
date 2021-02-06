input = [0, 3, 5, 6, 1, 2, 4]

#페이스북 기출
def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <=1:# 처음sum초깃값 0 * 이므로 or이후 추가
            multiply_sum += number
        else:
            multiply_sum *= number


    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)
# 5N 의 시간복잡도