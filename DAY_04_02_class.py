# DAY_04_02_class

class Info:
    def __init__(self, age): # 생성자
        print('init')
        # self.age = 25
        self.age = age

    def show(self):
        print('show', self, self.age)

    @property        # 변수처럼 사용하기 위해서-읽기 전용처럼 사용
    def my_age(self):
        return self.age


# a1, a2 = Info(), Info() # 생성자 __init__ 실행
a1, a2 = Info(27), Info(15) # self 외 나머지 파라미터 전달
print(a1)   # init

# 문제
# show 함수를 호출해 보세요.

# Info.show(123)  # 비정상 호출 함수
Info.show(a1)     # 정상 호출 함수 - Info를 담은 a1 unbound method
a1.show()         # 정상 호출 함수 - bound method

a1.age = 30
print('show()')
a1.show()
a2.show()
print('my_age()')
# print(a1.my_age()) # 함수 형태의 사용
# print(a2.my_age())
print(a1.my_age)     # property에 의해 변수처럼 사용
print(a2.my_age)
