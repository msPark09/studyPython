# DAY_04_04_slicing

a = [1,3,5,7,9,2,4,6,8,0]
print(a[len(a)-2],a[len(a)-1])  # 8 0
print(a[-2],a[-1])              # 8 0 음수 인덱스
print(a[3:5]) # 시작, 종료

# 문제
# 앞쪽 절반을 출력해 보세요
print(a[0:5])
print(a[0:len(a)//2])
print(a[:len(a)//2])  # 숫자 생략 가능

# print(a[-1:4:-1])

# 뒤쪽 절반을 출력해 보세요
print(a[5:10])
print(a[len(a)//2:len(a)])
print(a[len(a)//2:])

print(a[:])  # 전체

# 문제
# 짝수 번째만 출력해 보세요.
print(a[::2])      # 시작, 종료, 증감

# 홀수 번째만 출력해 보세요.
print(a[1::2])

# 문제
# 거꾸로 출력해 보세요
print(a[len(a)::-1])
print(a[len(a)-1::-1])
print(a[-1::-1])
print(a[::-1])

# print(a[3:3])
# i = 3
# while i<3:
#     print('hello')
#     i += 3

# 문제
# 짝수 번째만 거꾸로 출력해 보세요
print(a[::-2])

# 홀수 번째만 거꾸로 출력해 보세요
print(a[len(a)-2::-2])
print(a[-2::-2])

print('='*30)

a = [1,3,5,7,9,2,4,6,8,0]

b = a        # 포인터 저장 얕은 복사 shallow copy

c = a.copy() # 깊은 복사, deep copy
d = a[:]     # 깊은 복사, deep copy

a[0] = 99

print(a)
print(b)   # 같은 결과값

print(c)   # 다른 결과값
print(d)   # 다른 결과값

for i in d:
    print(i, end=' ')
print()

for i in reversed(d): # 모든 컬렉션 가능
    print(i, end=' ')
print()

for i in d[::-1]:   # 깊은 복사이기 때문에 메모리 차지함 # (slicing) list에서만 가능
    print(i, end=' ')
print()





































