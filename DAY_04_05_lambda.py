# DAY_04_05_lambda

def make_twice(n):
    return n * 2

f1 = make_twice
print(f1)     # <function make_twice at 0x0000000002063E18>
print(f1(2))  # 4

f2 = lambda n: n*2  # 한줄 함수 # return 필수
print(f2)     # <function <lambda> at 0x00000000022300D0>
print(f2(2))  # 4

print((lambda n:n*2)(2)) # 4

print('='*30)
def proxy(f, v):
    print(f(v))

proxy(make_twice, 3)
proxy(lambda n:n*2, 3) # 함수 포인터(코드 조립가능)

print('='*30)

import random
random.seed(1)

def make_randoms(size):
    ns =[]
    for _ in range(size):
        ns.append(random.randrange(100))
    return ns

a = make_randoms(10)
print(a)

# a.sort() # 정렬  # bound
# list.sort(a)     # unbound

# a = sorted(a)  # 복사된 list 전달
# print(a)

# 오름차순(ascending)
print(sorted(a)) # 저장하지 않으면 임시 sort 현 a는 정렬되지 않은 상태

# 내림차순(descending)
print(list(reversed(sorted(a))))
print(sorted(a, reverse=True))

def last_digit(n):
    # print(n)
    return n % 10
print(sorted(a, key=last_digit))   # 함수포인터 호출
                                   # [60, 72, 32, 63, 15, 17, 97, 97, 57, 8]
print(sorted(a, key=last_digit, reverse=True))   # 함수포인터 호출
print(sorted(a, key=lambda n:n%10, reverse=True))
def first_digit(n):
    return  n // 10
print(sorted(a, key=first_digit)) # [8, 17, 15, 32, 57, 63, 60, 72, 97, 97]

print('='*30)

colors =['Red', 'green', 'blue', 'YELLOW']

# 문제
# colors를 정렬해 보세요
print(sorted(colors))

# colors를 길이순으로 정렬해 보세요
print(sorted(colors, key=lambda n:len(n)))
print(sorted(colors, key=lambda n:n.lower()))

