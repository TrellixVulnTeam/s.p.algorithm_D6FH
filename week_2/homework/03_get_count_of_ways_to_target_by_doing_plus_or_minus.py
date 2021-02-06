numbers = [2, 3, 1]
target_number = 0
result = []  # 모든 경우의 수를 담기 위한 배열

# +2 +3 +1 = 6        +2 +3 +1
# +2 +3 -1 = 4              -1
# +2 -3 +1 = 0  타겟!  +2 -3 +1
# +2 -3 -1 = -2             -1
# -2 +3 +1 = 2        -2 +3 +1
# -2 +3 -1 = 0  타겟!        -1
# -2 -3 +1 = -4       -2 -3 +1
# -2 -3 -1 = -7             -1

#N의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
#N-1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를
#추가하면 된다.
def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(numbers):  # 탈출조건! current_index가 마지막에 다다랐을 때
        all_ways.append(current_sum)  # 마지막 인덱스에 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum + numbers[current_index], all_ways)
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum - numbers[current_index], all_ways)


get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result)
print(result)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!


numbers = [2, 3, 1]
target_number = 0
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):  # 탈출조건!
        if current_sum == target:
            global result_count #내부에서 외부에 있는 변수를 쓰겠다.
            result_count += 1  # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + numbers[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - numbers[current_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
print(result_count)  # 2가 반환됩니다!