shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 첫번째 방법
# O(N * logN) + O(M * NlogN) 총 O((M + N) * logN) 만큼의 시간복잡도가 걸린다.
def is_available_to_order(menus, orders):
    shop_menus.sort()# 정렬의 시간 복잡도는 배열의 길이를 N이라 하면
                     #  O(N * logN) 빅 오 표기 만큼의 시간복잡도를 갖는다.
    for order in orders: # O(M * NlogN) orders = M
        if not is_existing_target_number_binary(order, shop_menus):
            return False
    return True

def is_existing_target_number_binary(target, array):
    current_min = 0  # 배열의 index값  최솟값
    current_max = len(array) - 1  # 배열의 index값 최댓값
    current_guess = (current_min + current_max) // 2  # 시돗값
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
        current_guess = (current_max + current_min) // 2  # 시돗값 변경(업데이트)
    return False  # while문을 돌며 한번도 반복되지 않는다면 없다는 소리 이므로 return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)


# #두번째 방법 집합함수를 이용  ex) a = set([1, 2, 3, 4, 1, 2, 3])
# # 중복을 허용하지 않는 자료형     a = {1, 2, 3, 4}
# shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
# shop_orders = ["오뎅", "콜라", "만두"]
#
# # O(N) + O(M) = O(N + M) #경우에따라 이진탐색과 집합자료탐색 을 활용해야한다.
# def is_available_to_order(menus, orders):
#     menus_set = set(menus) #집합  O(N)
#     for order in orders:# m
#         if order not in menus_set:
#             return False
#     return True
#
#
# result = is_available_to_order(shop_menus, shop_orders)
# print(result)