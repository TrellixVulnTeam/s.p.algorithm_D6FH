def count_down(number):
    if number < 0: # 탈출조건 0 보다 작으면 return
        return
    print(number)       #number를 출력하고

    count_down(number - 1)# count_down 함수를 number - 1 인자를 주고 다시 호출한다.

count_down(60)