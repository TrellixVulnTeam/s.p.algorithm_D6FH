class LinkedTuple:# %8을 했을시 나머지 값은 값들의 충동을 방지하기위 링크드리스트를 이용함
    def __init__(self):
        self.items = list()

    # [("임의의key값", "test)] -> [("임의의key값2", "test33")]
    def add(self, key, value):# add("임의의key값", "test")
        # add("임의의key값", "test") 을 하면 self.items는 [("임의의key값", "test")]
        # add("임의의key값2", "test33") 을 하면 self.items는 [("임의의key값", "test"),("임의의key값2", "test33")]
        self.items.append((key, value))

    def get(self, key):# [("임의의key값", "test"),("임의의key값2", "test33")] 중에 원하는 key값을 입력시 해당 key의 값 items를 반환
        for k, v in self.items:
            if key == k:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []# [LinkedTuple(), ... ] 들어가 있는 상태, 각 원소의 키가 동일하면 똑같은 LinkedTuple 안에서 값들이 쭉쭉 늘어난다.
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        # LinkedTuple
        #[] 초기 빈 리스트
        #[(key, value)]
        self.items[index].add(key, value)
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)