# DAY_02_04_json
# http://www.jsontest.com/ㄴ
import json

a = '{"ip": "8.8.8.8"}'
print('a : ', a, type(a))
b = json.loads(a)  # json dictionary 로 변환
print('b : ', b, type(b), b['ip'])

# Q9
# dictionary b를 문자열로 다시 변환해 보세요.

c = str(b)   # json 형태의 문자열 가능성이 없음
print('c : ', c, type(c))
c = json.dumps(b) # json으로 변환
print('c2 : ', c, type(c))

dt = '''{
   "time": "03:53:25 AM",
   "milliseconds_since_epoch": 1362196405309,
   "date": "03-02-2013"
}'''

# Q10
# value만 뽑아서 출력해 보세요.

e = json.loads(dt)
print(e, type(e))

for i in e.values():
    print(i)

for k in e:
    print(e[k])

#import 아무데서나 가능
import requests
# data scraping module

url='http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
recvd = requests.get(url)
print(recvd)  #Response[200] : 정상 전송

print(recvd.text, type(recvd.text)) #type : str
text = bytes(recvd.text, 'iso-8859-1').decode('utf-8') # 문자 형식 확인 후 변환 가능
print(text)

# Q11
# 코드와 도시 이름만 출력해 보세요.

a = json.loads(text)
print(type(a)) #list

print('#1')
for i, dic in enumerate(a):
    print(dic['code'], ' : ', dic['value'])

print('#2')
for dic in a:
    print(dic['code'], ' : ', dic['value'])



















































