input = "abcabcabcabcdededededede"
# input = "ababcdcdababcdcd"

def string_compression(string):
    n = len(string)#문자열의 길이 저장
    compression_length_array = []# 최소길이 저장변수 생성
    for split_size in range(1, n // 2 + 1):# n // 2 + 1 = n // 2 이하
        # splited = []
        # for i in range(0, n, split_size):# 밑에있는 스플릿 반복과 동일한코드
        #     splited.append(string[i:i + split_size])

        splited = [string[i:i + split_size] for i in range(0, n, split_size)]
        print(splited)
        count = 1# 이전값과 자기값을 비교하는거기 때문에 1로 초기화
        compressed = "" # 압축해서 표현한 문자를 다시한번 compressed변수에다 저장함
        for j in range(1, len(splited)):# 이전값이랑 현재값 비교 하므로 1 부터 시작함
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                count += 1
            else:
                if count > 1:# 2개 이상부터는 압축을 해도 좋다
                    compressed += (str(count) + prev)# ex) 2 + ab -> 2ab
                else:# 1개라면 압축할 필요없이 추가
                    compressed += prev
                count = 1#반복이 끝나면 카운트 다시 1 로 초기화
        if count > 1:
            compressed += (str(count) + splited[-1])# splited[-1] == 꼬다리값, 마지막 남은값
        else:
            compressed += splited[-1]
        compression_length_array.append(len(compressed))
        print(compressed)
    return min(compression_length_array)


print(string_compression(input))  # 14 가 출력되어야 합니다!