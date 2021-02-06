seat_count = 9
vip_seat_array = [4, 7]#고정 이므로 세구간에서 나오는 경우의 수를 다 곱한다.
#고정된 좌석을 제외하고 자리를 옮기는데 최대 한 좌석만 이동가능

#  [1, 2]
# [1, 2] [2, 1] 총 2개
#
#  [1, 2, 3]
# [1, 2, 3] [2, 1, 3] [1, 3, 2] 총 3개
#
# [1, 2, 3, 4]
#  [1, 2, 3, 4] [1, 2, 4, 3] [1, 3, 2, 4] [2, 1, 3, 4] [2, 1, 4, 3] 총 5개
#
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5] [1, 2, 3, 5, 4] [2, 1, 3, 4, 5] [2, 1, 3, 5, 4]
# [1, 2, 4, 3, 5] [2, 1, 4, 3, 5] [2, 1, 3, 4, 5] [1, 3, 2, 4, 5]  총 8개

#  피보나치 수열
memo = {
    1: 1,      # 이 문제에서는 Fibo(1) = 1, Fibo(2) = 2 로 시작한다.
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1# 고정된 좌석 다음칸으로 넘겨준다.

    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)# 고정된좌석7 이후의 좌석 배열 경우의수
    all_ways *= count_of_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))