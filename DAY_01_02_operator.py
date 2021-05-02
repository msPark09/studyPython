# DAY_01_02_operator.py

# 변수 타입 유동적으로 변경 가능
# 해당 변수 자료형 정해지지 않음

# 연산 : 산술, 관계, 논리
# 산술 : + - * / ** // %

a, b = 7, 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b) # 7^3
print(a//b) # 몫 : 정수형 7/3 (정수 나눗셈) - 타입지정 없음 => 정수형, 실수형 나눗셈 존재
print(a%b)

# Q3
# 2자리 양수를 뒤집어 보세요.
# 27 -> 72
a=27
b=a%10*10+a//10
print(a, b)

# Q4
# 4자리 양수를 뒤집어보세요.
# 1234 -> 4321
a=1234
# a,b,c,d =1,2,3,4
# print(d,c,b,a, sep='')
a1 = a//10**3
# a2 = a//100%10
a2=(a-(a1*10**3))//(10**2)
a3 = a%100//10
a4 = a%10
print(a1+a2*10+a3*100+a4*1000)

b=1234
b12=b//100
b34=b%100
b1 = b12//10+b12%10*10
b2 = b34//10+b34%10*10
print(b1+b2*100)

# 관계 : > >= < <= == !=
a, b = 7, 3
print(a>b)   #true
print(a>=b)  #true
print(a<b)   #false
print(a<=b)  #false
print(a==b)  #false
print(a!=b)  #true

# Q5
# 어떤 학생의 나이가 10인지 알려주세요.
age = 23
print(age >= 10 and age < 20)  #false

age = 13
print(10<= age < 20)  #true

# 논리 : and or not
print(True and True)   #true
print(True and False)  #false
print(False and True)  #false
print(False and False) #false

















