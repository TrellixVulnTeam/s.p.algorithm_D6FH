import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30
#현재 재고가 바닥나는 시점 이전까지 받을 수 있는
#라면 중 제일 많은 라면을 받는 게 목표이다.
#제일 많은 -> 정렬하면되겠다.
#1. 현재 재고의 상태에 따라 최곳값을 받아야 한다.(동적으로 변경되는 상태)
#2. 제일 많은 값만 가져가면 된다.
#1. 데이터를 넣을 때마다 최솟/최댓값을 동적으로 변경시키며
#2. 최솟/최댓값을 바로 꺼낼 수 있는 자료구조
# heap 을 쓰면 된다.

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0 #정답반환 변수 초기화
    current_day_index = 0
    max_heap = []

    while stock < k: #stock이 k 보다 작을때까지 공급량 추가
        for date_index in range(current_day_index, len(dates)):
            print(date_index, dates[date_index], stock, supplies[date_index])
            if dates[date_index] <= stock:
                heapq.heappush(max_heap, -supplies[date_index])
            else:
                current_day_index = date_index
                break
        answer += 1
        stock += -heapq.heappop(max_heap)
        print("stock is", stock)
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))