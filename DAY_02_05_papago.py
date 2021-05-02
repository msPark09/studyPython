# DAY_02_05_papago

import requests
import json

# header : 접근 경로 확인 가능
# header 분석으로 접근경로 분석
# Accept:*/*
# Accept-Encoding:gzip, deflate
# Accept-Language:ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4
# Connection:keep-alive
# Content-Length:128
# content-type:application/x-www-form-urlencoded; charset=UTF-8
# Cookie:npic=WSEGUAaBDolPJOBUvn+I6o80bio82yM6wb1JFn0QXdWNuOoeUl2/BHTn50D1oH7SCA==; NNB=E5PDGGKJKA5VS; nx_ssl=2; wcs_bt=dccae51cc9ffb4:1497163377|c3e93c6907418c:1497163354
# Host:labspace.naver.com
# Origin:http://labspace.naver.com
# Referer:http://labspace.naver.com/nmt/
# User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36
# x-naver-client-id:labspace

url = 'http://labspace.naver.com/nmt/'
recvd = requests.get(url) # get 방식
headers = {'x-naver-client-id' : 'labspace'}
payload = dict(source='ko',
               target='en',
               text='후라보노껌은 맛있습니다.')

url = 'http://labspace.naver.com/api/n2mt/translate'
recvd = requests.post(url, data=payload, headers=headers) # post 방식
print(recvd)
print(recvd.text)

# Q12
# 번역 결과만 출력해 보세요.
a = json.loads(recvd.text)
print(a, type(a))
print(a.keys())
print(a['message'].keys())
print(a['message']['result'].keys())
b = a['message']['result']['translatedText']
print(b, type(b))

# Q13
# 위의 코드를 함수로 변환해 보세요.
# 한글 -> 영어, 영어 -> 한글
import re

def papago(text):
    find_text = re.findall(r'[A-Za-z]+', text)
    headers = {'x-naver-client-id': 'labspace'}
    # if  len(find_text):
    #     source = 'en'
    #     target = 'ko'
    # else:
    #     source = 'ko'
    #     target = 'en'
    # payload = dict(source=source, target=target, text=text)
    payload = dict(source='ko', target='en', text=text)
    if len(find_text):
        payload['source']='en'
        payload['target']='ko'
    #dict를 먼저 만든 후 입력 방식

    url = 'http://labspace.naver.com/api/n2mt/translate'
    recvd = requests.post(url, data=payload, headers=headers)  # post 방식

    item = json.loads(recvd.text)
    return item['message']['result']['translatedText']

print('-'*10)
text = '안녕?'
print(text,'->',papago(text))

















