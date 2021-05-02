# Day_02_01_function.py

# 프로그램 : 코드(함수), 데이터(변수)
# 함수 : 코드 조각

# 팀장 --> 데이터 --> 사원 : 매개변수
# 팀장 <-- 데이터 <-- 사원 : 반환값

# 매개변수 없고, 반환값 없고.
def f_1():
    print('f_1')

f_1()

# 매개변수 있고, 반환값 없고.
def f_2(a, b):         # a = 12
    print('f_2', a + b)

f_2(12, 34)      # f_2 46
f_2('12', '34')  # f_2 1234
# f_2(12, '34')  # 자료형 맞지 않아 연산 안됨.

# 매개변수 없고, 반환값 있고.
def f_3():
    print('f_3')

a = f_3()
print(a) #return 값 없음 print 시 None

def f_4():
    print('f_4')
    return 7

b = f_4()     # f_4
print(b)      # 7
print(f_4())  # f_4 \n 7
f_4()         # f_4

# 매개변수 있고, 반환값 있고.
# Q1
# 2개의 정수 중에서 큰 숫자를 찾으세요.
def max2(a, b):
    # if a > b:
    #     return a
    # else:
    #     return b

    # if a > b:
    #     return a
    # return b

    if a > b:
        b = a
    return b

print(max2(2, 9))
print(max2(9, 2))

def dummy():
    print(t)

t = 12 # 전역변수 사용 거의 없음
dummy()

# Q2
# 4개의 정수 중에서 큰 숫자를 찾으세요.

def max4(a, b, c, d):
    # pass  # 함수 내 내용 없을 경우 사용 가능

    # 배열방식
    # t = a[0]
    # n = 4
    # while n > 0:
    #     if t < a[n]:
    #         t = a[n]
    #     n -= 1

    # 1
    # if a < b : a = b
    # if a < c : a = c
    # if a < d : a = d
    # return  a

    # 2
    # t = max2(a, b)
    # f = max2(c, d)
    # return max2(t , f)

    # 3
    # return max2(max2(a, b), max2(c, d))

    # 4
    return max2(max2(max2(a, b),c),d)  # python 성능상 고려 : 우선순위 하위

a, b, c, d = 17, 8, 46, 9
print(max4(a,b,c,d))







