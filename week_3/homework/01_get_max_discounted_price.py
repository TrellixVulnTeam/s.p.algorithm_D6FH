shop_prices = [30000, 2000, 1500000]# 상품의 가격
user_coupons = [20, 40]# 쿠폰, 할인율의 단위는 %이다.


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse = True)
    coupons.sort(reverse = True)

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100# 할인율이기 때문에 100 에서 쿠폰할인율을 빼준다.
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):#상품의 가격 끝까지 반복 쿠폰적용안돼는 값이 제일싼 2000
        max_discounted_price += prices[price_index]
        price_index += 1
    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.