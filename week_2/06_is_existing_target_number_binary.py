#이진 탐색
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min = 0 # 배열의 index값  최솟값
    current_max = len(array) - 1 # 배열의 index값 최댓값
    current_guess = (current_min + current_max) // 2 #시돗값
    find_count = 0

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2 #시돗값 변경(업데이트)
    return False# while문을 돌며 한번도 반복되지 않는다면 없다는 소리 이므로 return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)


