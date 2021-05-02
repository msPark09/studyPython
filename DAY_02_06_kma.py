# DAY_02_06_kma
# rss : xml의 한 종류
# html, xml 파싱 : https://cryptosan.github.io/pythondocuments/documents/beautifulsoup4/

import re
import requests

url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
recvd = requests.get(url)
print(recvd, recvd.text)

temp = re.findall(r'<province>.+</province>', recvd.text) # default같은 라인에 있는 문자열 검색
print(temp)
print(len(temp))

# Q14
# location 영역을 찾아보세요.

# .+ : 탐욕적, greedy 검색
locations = re.findall(r'<location wl_ver="3">.+</location>', recvd.text, re.DOTALL) # DOTALL : 여러 라인에 걸친 문자열 검색
# ? : 비탐욕적
locations = re.findall(r'<location wl_ver="3">.+?</location>', recvd.text, re.DOTALL) # list 결과
print(len(locations))

for loc in locations:
    print(loc)

# Q15
# province 와 city를 찾아보세요.

for loc in locations:
    province = re.findall(r'<province>(.+?)</province>', loc, re.DOTALL)
    city = re.findall(r'<city>(.+)</city>', loc)
    print(province)
    print(city)
    print(province[0])
    print(city[0])

# Q15
# data를 찾아보세요
# for loc in locations:
    data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
    print(data)

    # < mode > A02 < / mode >
    # < tmEf > 2017 - 06 - 14
    # 00: 00 < / tmEf >
    # < wf > 구름많음 < / wf >
    # < tmn > 18 < / tmn >
    # < tmx > 27 < / tmx >
    # < reliability > 보통 < / reliability >
# Q16
# mode, tmEf, wf, tmn, tmx, reliability를 찾아보세요.
    for datum in data:
        # mode = re.findall(r'<mode>(.+)</mode>', datum)
        # tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
        # wf = re.findall(r'<wf>(.+)</wf>', datum)
        # tmn = re.findall(r'<tmn>(.+)</tmn>', datum)
        # tmx = re.findall(r'<tmx>(.+)</tmx>', datum)
        # reliability = re.findall(r'<reliability>(.+)</reliability>', datum)

        # print('mode',':', mode[0])
        # print('tmEf',':', tmEf[0])
        # print('wf',':', wf[0])
        # print('tmn',':', tmn[0])
        # print('tmx',':', tmx[0])
        # print('reliability',':', reliability[0])

# 숫자 신경쓰지 말것 error : 변환 로직만 확인
        item = re.findall(r'<mode>(.+)</mode>.+?<tmEf>(.+)</tmEf>', datum, re.DOTALL)
        item = re.findall(r'<.+?>(.+)</.+?>.+?<.+?>(.+)</.+?>', datum, re.DOTALL)
        item = re.findall(r'<.+?>(.+?)</.+?>' * 2, datum, re.DOTALL)
        item = re.findall(r'<.+?>(.+?)</.+?>', datum, re.DOTALL)
        mode, tmEf = item[0]
        print(mode, tmEf)







