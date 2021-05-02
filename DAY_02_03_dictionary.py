#DAY_02_03_dictionary

a1, a2, a3 = {}, {1}, {1: 2}
print(a1, type(a1))
print(a2, type(a2))
print(a3, type(a3)) # dictionary -> map 형태

s1 ={3,5,1,3,5,1,3,5,1}  # set
print(s1) # {1, 3, 5} - 중복요소 제거되어 나옴

# Q6
# 리스트를 unique 하게 만들어 주세요.(중복요소 제거)

s2 =[3,5,1,3,5,1,3,5,1]  # list
print(s2)
s2 = list(set(s2))  # 데이터 변환 collection 변환 가능
print(s2)

d = {'name': 'kim', 'age': 20}
d = dict(name='kim', age=20)  # key 값 문자열 고정
print(d)
print(d['name'], d['age']) # kim 20

d['addr'] = 'suji' # append 없이 가능 - insert
print(d)

d['addr'] = 'seocho' # 데이터 수정 - update
print(d)

print(d.keys())
print(d.values())
print(d.items())

# Q7
# keys, valuse, items 함수를 for문과 연동시켜 보세요.
for k in d.keys():
    print(k , ' : ' , d[k])

for v in d.values():
    print(v)
for i in d.items():
    print(i)
for k, v in d.items():  # 다중치환 가능
    print(k, ' : ' ,v)

# Q8
# 아래 코드에 enumerate 함수를 추가해 보세요.
for i in enumerate(d.items()):
    print(i, i[0], i[1], i[1][0], i[1][1])  # 2차 배열처럼 사용 가능

for i, kv in enumerate(d.items()):
    print(i, kv, kv[0], kv[1])

# for i, k, v in enumerate(d.items()):
#     print(i, k, v)

for i, (k, v) in enumerate(d.items()): # 형식만 맞으면 그냥 써서 사용 가능
    print(i,'-', k, ':' ,v)















