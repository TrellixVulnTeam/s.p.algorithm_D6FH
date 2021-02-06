class Dict:
    def __init__(self):
        self.items = [None]*8

    def put(self, key, value):# key와 value 추가
        index = hash(key) % len(self.items)#key의 해쉬값 을 현재 배열의 최대길이(len(self.items)로 %연산 그러면 index 값은 0~7사이 값을 갖는다.
        self.items[index] = value# 그 값에 value를 넣어 업데이트
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]# 인덱스를 바로 key로 이용해서 반환

my_dict = Dict()
my_dict.put("test", 3)# test를 key값으로 3을 value에 저장하고
print(my_dict.get("test"))# test란 key 값을 이용해서 value를 가져와 출력해 보겠다라는 의미