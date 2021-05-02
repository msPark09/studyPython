# DAY_01_01_basic.py

## 주석처리
# line copy : ctrl + c
# 현재파일 실행 : shift + ctrl + f10

print('hello, python!')

# Q1
# hello,python!을 3회 출력하는 코드를
# 3가지 만들어 보세요.
a = 'hello, python!'
print('#1')
#print('hello, python!\n' * 3)
#String 곱하기 처리 가능
print((a) * 3)

print('#2')
#2
i=0
while i < 3:
    # print('hello, python!')
    print(a)
    i+=1

print('#3')
#3
for j in range(3):
    # print('hello, python!')
    print(a)

print('#4')
print('hello' 'hello' 'hello')
print("hello" "hello" "hello")
print(a,a,a)
print("hello, 'python!'")
print('hello, "python!"')
print('hello, \'python!\'')

print('-'*50)

# 프로그램 : 코드(함수), 데이터(변수)
# 정수 / 실수  / 문자열 / 논리값
# int / float / str   / bool
print(12, 3.14,'hello', True)
print(type(12), type(3.14), type('hello'), type(True))

print('-'*50)

a=3
print(a,3)

a=7
print(a,3)

a=3
b=7
print(a, b)

# Q2
# a 와 b의 값을 교환해 보세요
# c=a
# a=b
# b=c

# 동시에 여러 데이터 대입 가능
# 다중치환
a, b = b, a
print(a, b)

# 선언도 가능
a, b = 4, 5
# a = 3 ; b = 4
print(a, b)
# 한줄 단위로 인터프리트






























