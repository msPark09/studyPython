# DAY_01_03_if

a = 17
if a % 2 != 0:
    print('홀수')
    #tab으로 구문 구분
    if a % 7:            # 0 : false 0 외의 숫자 : true
        print(a%7, '7의 배수가 아니다', sep='--')
    else:
        print('7의 배수')
    print('if 끝!!')
else:
    print('짝수')

a = 0
if a:   print('참')
else:   print('거짓')

# 형변환

print('123', 123)
print('123'+'123')
print(123 + 123)
print(int('123')+123)
print('123'+str(123))

# Q6
# 입력 받은 정수가 양수인지 음수인지 0인지 알려주세요.

a='123'
# a=input()   # input으로 받을 때는 String
print(a)
print(type(a))
a=int(a)

print('#1')
if a > 0:
    print('양수')
elif a < 0:
    print('음수')
else:
    print('0')

print('#2')
if a != 0:
    if a > 0:
        print('양수')
    else:
        print('음수')
else:
    print('0')

print('#3')
if a > 0:
    print('양수')
if a < 0:
    print('음수')
if a == 0:
    print('0')

# 인터프리터 무시 : 공백(space, tab, enter)

# Q7
# 0~999 사이의 정수가 몇 자리인지 알려주세요.
# 27 -> 2자리
a=157

print('#1')
if a > 99:
    print('3자리')
elif a > 9:
    print('2자리')
else:
    print('1자리')

print('#2')
if a < 10:
    print('1자리')
elif a < 100:
    print('2자리')
else:
    print('3자리')

# Q8
# 'hello'를 지정한 횟수만큼 출력해 보세요.
# 0<= n <=3

print('#1')
n = 2
i = 0
while i < n:
    print('hello')
    i += 1

print('#2')
i = 0
while 1:
    print('hello')
    i += 1
    if i == n:
        break

print('#3')
print('hello\n' * n)

print('#4')
n=2
while 1:
    if n > 0:
        print('hello')
        n -= 1
    else:
        break























