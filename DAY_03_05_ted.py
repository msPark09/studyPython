# DAY_03_05_ted

# https://www.ted.com/talks

import requests
import re

url="https://www.ted.com/talks"
recvd= requests.get(url)

# print(recvd)
# print(recvd.text)

# 문제
# 테드 페이지를 강연자, 제목, 날짜, 분류로 정리해서 출력해 주세요.


talks = re.findall(r"<div class='media__message'>(.+?)</div>", recvd.text, re.DOTALL)
# names = re.findall(r'[A-Z]*[a-z]+', db)
# print(talks, len(talks),sep='\n')
for talk in talks:
    # print(talk)
    # 문제
    # 강연자와 제목 등을 출력해 보세요.
    talker = re.findall(r"<h4 class='h12 talk-link__speaker'>(.+?)</h4>", talk, re.DOTALL)
    talker = talker[0].strip()

    title  = re.findall(r"<a.+?>(.+?)</a>", talk, re.DOTALL)
    title = title[0].strip()

    meta   = re.findall(r"<span class='meta__val'>(.+?)</span>", talk, re.DOTALL)
    # 문제
    # 아래 있는 날짜와 분류를 깔끔하게 정리해 주세요.

    date = meta[0].strip()
    if len(meta) == 2:
        cat = meta[1].strip()

    # print(talker)
    # print(title)
    # # print(meta)
    # print(date, cat, sep=' / ')

    print(talker, title, date, cat, sep='::')

# 문제
# 위 코드를 특정 페이지를 가져올 수 있는 함수로 변환해 보세요.
def find_ted(page, sort):

    url = "https://www.ted.com/talks?page={}&sort={}"
    recvd = requests.get(url.format(page, sort))

    talks = re.findall(r"<div class='media__message'>(.+?)</div>", recvd.text, re.DOTALL)

    # if len(talks)==0:
    #     return False     # 처리 데이터 없음!

    # if not len(talks):   # 길이 0
    #     return False

    if not talks:          # 비어있는 리스트 False
        return False

    for talk in talks:

        talker = re.findall(r"<h4 class='h12 talk-link__speaker'>(.+?)</h4>", talk, re.DOTALL)
        talker = talker[0].strip()

        title = re.findall(r"<a.+?>(.+?)</a>", talk, re.DOTALL)
        title = title[0].strip()

        meta = re.findall(r"<span class='meta__val'>(.+?)</span>", talk, re.DOTALL)


        date = meta[0].strip()
        if len(meta) == 2:
            cat = meta[1].strip()

        print(talker, title, date, cat, sep='::')
        return True

# 봇의 형태 => 사이트별로 정보 수집
# for page in range(1,3):
#     print('='*15, page ,'='*15)
#     find_ted(page)
# page =1
# while find_ted(page, 'funny'):            # 페이지 숫자에 관계없이 수집 가능
#     print('='*15, page ,'='*15)
#     page += 1

# <optgroup label="Sort by..."
# Newest="newest"
# Oldest="oldest"
# Most viewed="popular"
# Jaw-dropping="jaw-dropping"
# Funny="funny"
# Persuasive="persuasive"
# Courageous="courageous"
# Ingenious="ingenious"
# Fascinating="fascinating"
# Inspiring="inspiring"
# Beautiful="beautiful"
# Informative="informative">

sortBy = ['newest','oldest','popular','jaw-dropping','funny','persuasive','courageous','ingenious','fascinating','inspiring','beautiful','informative']

for sort in sortBy:
    print('='*10, sort, '='*10)
    page = 1
    while find_ted(page, sort):  # 페이지 숫자, 정렬에 관계없이 모두 수집 가능
        print('=' * 15, page, '=' * 15)
        page += 1
