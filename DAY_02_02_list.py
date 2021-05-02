# DAY_02_02_list

# 배열 없음 -> 컬렉션 사용

# collection : list, tuple, set, dictionary
#               []     ()   {}     {}

a = [1, 3, 5]
print(a, type(a))
print(a[0], a[1], a[2])

a[0] = 99
a[2] = a[0]
print(a)

for i in range(3):
    print(i, ':' , a[i])

# a[3] = 13 # a index 초과
# print(a)
a.append(13)
print(a)
for i in range(len(a)):  # list length : len()
    print(i, ' : ' ,a[i])

import random
# random.seed(1) # 난수 고정-개발시 유용

for _ in range(10):   # place holder : _ 제공하여 변수 네이밍 줄임
    # print(random.randrange(100), end=' ')
    print(random.randrange(30, 100, 5), end=' ')  # 30부터 100까지 5단위
    # print(_) # 변수임
print()

# Q4
# 난수 10개가 들어있는 리스트를 반환하는 함수를 만드세요.
b=[]
for _ in range(10):
    b.append(random.randrange(100))
print(b, type(b), len(b))

def make_randoms(size):
    # a = [0] * size
    # for i in range(size):
    #     a[i] = random.randrange(100)
    a = []
    for _ in range(size):
        a.append(random.randrange(100))
    return a

print(make_randoms(10))

# Q5
# 리스트에서 가장 큰 값과 두번째로 큰 값을 찾는 함수
def max2(a, b):
    if a < b:
        a = b
    return a

def list_max(b):
    # for i in range(len(b)):
    #     if (i + 1) == len(b):
    #         break
    #     elif i != mi:
    #         mn1 = max2(b[i], b[i+1])
    #         mi = i

    mn1, mn2 = 0, 0
    # for i in range(len(b)):
    #     mn1 = max2(mn1,b[i])
    # return mn1
    for i in range(len(b)):
        if mn1 < b[i]:
            mn2 = mn1
            mn1 = b[i]
        elif mn2 < b[i]:
            mn2 = b[i]
    return mn1, mn2  # 튜플형태로-시스템 내에서 사용 return 개수 제한 없음

print(list_max(b))

t = list_max(b)
print(t, t[0], t[1]) # list 동일

t1, t2 = list_max(b)  # 다중치환
print(t1, t2)

# t[0] = 99     # 내용 변경 불가
# t.append(99)  # append 변경 불가

t3, t4 = 8, 9
t = 8, 9          # packing
t5, t6 = t        # unpacking
print(t3, t4, t, t5, t6)

for i in b:     # foreach문과 같은 형태
    print(i, end=' ')
print()
# range, list : interable

# Q6
# b를 거꾸로 출력해 보세요.

for i in reversed(b):
    print(i, end=' ')
print()




























