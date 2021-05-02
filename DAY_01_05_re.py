# DAY_01_05_re

#RegularExpress (정규표현식)
import re

a = '12 34 56'
print(a)

a = '12\n34\n56'
print(a)

a = '12\n' \
    '34\n' \
    '56\n'
print(a)

a = '12\n'
'34\n'  # 그냥 코드에 작성된 데이터
'56\n'
print(a)

a='''12
     34
     56'''
print(a)

#'''뒤에 개행문자 입력되어 있음
a=''' 
12
34
56'''
print(a)

a='''12
34
56'''
print(a)

#    phone   name  ID
db='''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''

print(db)

temp = re.findall(r'[0-9]',db) # r : row (정규표현식 표시)
                               # db에서 r'내의 값' find
print(temp)

numbers = re.findall(r'[0-9]+', db)
print(numbers)

# Q9
# 이름을 찾으시오

names = re.findall(r'[A-Z]*[a-z]+', db)
names = re.findall(r'[A-Za-z]+', db)
# names = re.findall(r'[A-Z|a-z]',db)
names = re.findall(r'[A-Z][a-z]+', db) # 영문이름 특성에 따른 표현
# names = re.findall(r'[A-z]+', db)  # 특수문자 포함 search
print(names)

# Q10
# T로 시작하는 이름만 출력하세요.
names = re.findall(r'T[a-z]+', db)
print(names)

# T로 시작하지 않는 이름만 출력하세요.
names = re.findall(r'[^T][a-z]+', db)  #Tony 의 ony 포함
names = re.findall(r'[A-SU-Z][a-z]+',db)
print(names)



















