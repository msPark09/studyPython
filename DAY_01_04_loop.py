# DAY_01_04_loop

# 1 3 5 7 9    1, 9, 2
# 0 1 2 3 4    0, 4, 1
# 4 3 2 1 0    4, 0, -1
print('#1')
n=5
i=0             # 시작
while i < n:    # 종료
    print(i, end=' ')
    i += 1      # 증감

print('\n#2')
n=5
i=0             # 시작
while n > i:    # 종료
    n -= 1      # 증감
    print(n, end=' ')
print()

print('for _ in range')
for i in range(0,5,1):  # 시작, 종료, 증감
    print(i, end=' ')
print()

for i in range(0,5):
    print(i, end=' ')
print()

for i in range(5):
    print(i, end=' ')
print()
# default - 시작 : 0, 증감 : 1

# Q3
# 0~99까지의 정수를 거꾸로 출력해 보세요.
print('#1')
for i in range(99,0,-1):
    print(i, end=' ')
print()
print('#2')
n=99
for i in range(n):
    print(n, end=' ')
    n -= 1
print()

print('#3')
for i in range(100-1,-1,-1):
    print(i, end=' ')
print()

print('#4')
for i in reversed(range(10)):  # 반대순서 reversed 함수 제공
    print(i, end=' ')
