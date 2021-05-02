# Day_02_06_kma.py
import re
import requests

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
recvd = requests.get(url)
# print(recvd)
# print(recvd.text)

# temp = re.findall(r'<province>.+</province>', recvd.text)
# print(temp)
# print(len(temp))

# 문제
# location 영역을 찾아보세요.

# .+ : 탐욕적, greedy
# .+? : 비탐욕적, non-greedy
locations = re.findall(r'<location wl_ver="3">.+?</location>',
                       recvd.text,
                       re.DOTALL)
# print(locations)
# print(len(locations))

for loc in locations:
    # print(loc)

    # 문제
    # province와 city를 찾아보세요.
    prov = re.findall(r'<province>(.+)</province>', loc)
    city = re.findall(r'<city>(.+)</city>', loc)
    print(prov[0], city[0])

    # 문제
    # data를 찾아보세요.
    data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
    # print(data)
    # print(len(data))

    for datum in data:
        # print(datum)

        # 문제
        # mode, tmEf, wf, tmn, tmx, reliability를 찾아보세요.
        # mode = re.findall(r'<mode>(.+)</mode>', datum)
        # tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
        # wf   = re.findall(r'<wf>(.+)</wf>', datum)
        # tmn  = re.findall(r'<tmn>(.+)</tmn>', datum)
        # tmx  = re.findall(r'<tmx>(.+)</tmx>', datum)
        # reli = re.findall(r'<reliability>(.+)</reliability>', datum)

        # print(mode[0], tmEf[0], wf[0], tmn[0], tmx[0], reli[0])

        # item = re.findall(r'<mode>(.+)</mode>.+?<tmEf>(.+)</tmEf>.+?<wf>(.+)</wf>.+?<tmn>(.+)</tmn>.+?<tmx>(.+)</tmx>.+?<reliability>(.+)</reliability>',
        #                   datum, re.DOTALL)
        # print(item[0])
        # item = re.findall(r'<.+?>(.+)</.+?>.+?'
        #                   r'<.+?>(.+)</.+?>.+?'
        #                   r'<.+?>(.+)</.+?>.+?'
        #                   r'<.+?>(.+)</.+?>.+?'
        #                   r'<.+?>(.+)</.+?>.+?'
        #                   r'<.+?>(.+)</.+?>',
        #                   datum, re.DOTALL)
        # item = re.findall(r'<.+?>(.+)</.+?>.+?' * 6,
        #                   datum, re.DOTALL)
        #
        # mode, tmEf, wf, tmn, tmx, reli = item[0]
        # print(mode, tmEf, wf, tmn, tmx, reli)

        item = re.findall(r'<.+?>(.+?)</.+?>',
                          datum, re.DOTALL)
        print(item)

# <mode>A02</mode>
# <>2017-06-14 00:00</tmEf>
# <wf>구름많음</>
# <tmn>18</>
# <tmx>27</>
# <reliability>보통</>








