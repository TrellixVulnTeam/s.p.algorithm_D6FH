class JSS:
    def __init__(self):
        self.name = input("이름 : ")
        self.age = input("나이 : ")
    def show(self):
        print("나의 이름은 {}, 나이는 {}세입니다.".format(self.name, self.age))
a = JSS()
a.show()

class JSS2(JSS):
    def __init__(self):
        super().__init__()
        self.gender = input('성별 : ')
    def show(self):
        print("나의 이름은 {}, 성별은 {}, 나이는 {}세입니다.".format(self.name, self.gender, self.age))

a = JSS2() # a --> self __init__ 안에있는 내용 실행
a.show()