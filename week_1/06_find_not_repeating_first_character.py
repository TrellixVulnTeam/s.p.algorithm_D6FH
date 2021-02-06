input = "abadabac"


def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0]*26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] +=1
    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))
    for char in string:                           # for 문 있고 없고 차이 알기
        if char in not_repeating_character_array: # 반복되지않는 첫번째 알파벳
            return char                           #문자열을 순차적으로 돌다 처음 index가 1인 문자를 바로 반환하라
    print(not_repeating_character_array)
    return "-"


result = find_not_repeating_first_character(input)
print(result)