# DAY_03_02_function
# pep8 : https://spoqa.github.io/2012/08/03/about-python-coding-convention.html


def not_used():
    def f_1(a, b, c):
        print(a, b, c, end='\n', sep='_')
        print(a, b, c, sep='_', end='\n')

    f_1(1,2,3)         # position argument
    f_1(a=1, b=2, c=3) # keyword argument
    f_1(b=2, c=3, a=1) # 순서 변경 가능
    f_1(1, b=2, c=3)   # argument 혼합가능

    # f_1(a=1, 2, c=3)   # keyword는 position 뒤만 가능
    # tab 기능으로 함수 안에 넣기

    def f_2(a,b=0,c=0):    # default argument
        print(a, b, c)

    f_2(1,2,3)
    f_2(1)                  # argument 생략시 default 값
    f_2(1,2)
    f_2(a=1)
    f_2(1, b=2)
    f_2(b=1, a=2)

    def f_3(*args):    # 가변인자 (packing을 통해 인자 가변으로 받기)
        print(args)
        print(*args)   # unpacking

    f_3()
    f_3(1, 2)
    f_3([1,2,3], (1,2), 'hello')
    f_3(1)                # tuple 형태로 전달
    f_3('hello Python')   # print 시 단순 자료형과 구분하기 위해 (1,) 표시

    a = [1, 3, 5]
    print(a)   # packing   [1, 3, 5]
    print(*a)  # unpacking 1 3 5
    print(*a, sep=',')  # unpacking 1,3,5

    def f_4(**kwargs):    # keyword argument 가변인자 (packing)
        print(kwargs)
        # f_5(kwargs)     # error
        f_5(**kwargs)     # unpacking
        f_5(a=kwargs)     # keyword로 전달

    def f_5(**kwargs):    # 인터프리터이기 때문에 선언시 save 호출시 실행되어 순서는 상관 없음
        print(kwargs)

    f_4()
    # f_4(1)
    f_4(a=1,b=2)
    f_4(a=1,b=2,c=3) # dictionary {'a': 1, 'b': 2, 'c': 3}
    f_4(a={'b':2, 'c':3})


d = dict(a=1, b=2)
print(d, type(d))

# dict 함수 만들기
def f_6(**kwargs):
    return kwargs
e = f_6(a=1, b=2)
print(e, type(e))

























