a, b, c = map(int, input().split())

list = [a, b, c]


def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num


a = find_max_num(list)


if (a < b + c):
    print('Valid')
else:
    print('Invalid')