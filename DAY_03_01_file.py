# DAY_03_01_file

# 파일 : 텍스트, 바이너리
# 텍스트 : 글자
#         txt, csv, smi, py, java...
# 바이너리 : 특정 형식 존재
#           xls, ppt, doc, mp4, jpg, exe...

# 경로 : 절대경로, 상대경로
# 절대경로 : 드라이브 제목 or 루트(/)부터 시작하는 경로
# ex) C:\Users.....\python
# 상대경로 : 현재 폴더부터 시작하는 경로
# 현재 폴더 : 실행 파일 또는 실행한 파이썬 파일이 있는 폴더



# import this # the zen of python 출력

def read_1():
    # f = open('DAY_03_01_file.py', 'r', encoding='utf-8')  # C code 유사
    # f = open('Data\zen.txt', 'r', encoding='utf-8')
    f = open('../python/Data/zen.txt', 'r', encoding='utf-8')

    lines = f.readlines()
    print(lines)

    # for i in range(len(lines)):
    #     print(lines[i], end='')

    for line in lines:
        line = line.strip() # 개행문자 삭제
        print(line)

    f.close()

read_1()

a = '\n\n\t\t AA BB AA \t\t\n\n'
print('[',a,']')
print('[',a.strip(),']')  # trim과 같이 동작(직접 작성한 특수문자도 제거) 양쪽 공백 제거

print('#'*30)

def read_2():
    f = open('Data/zen.txt', 'r', encoding='utf-8')

    while True:
        line = f.readline()
        if len(line) == 0:  # EOF(End Of File)
            break
        print(line.strip())
    f.close()
read_2()


print('#'*30)

def read_3(filename):
    # f = open('Data/zen.txt', 'r', encoding='utf-8')
    f = open(filename, 'r', encoding='utf-8')

    rows = []
    for line in f:
        print(line.strip())
        rows.append(line.strip())
    f.close()
    return rows

read_3('Data/zen.txt')

print('4','#'*30)

def read_4(filename):
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            print(line.strip())

read_4('Data/zen.txt')

def write():
    f = open('Data/zen_write.txt', 'w', encoding='utf-8')

    f.write('Hello')
    f.write('\n')
    f.write('Python')

    f.close()
write()


# 문제
# kma.txt 파일에 저장해 보세요.
import re
import requests

def write2(filename):
    f = open(filename, 'w', encoding='utf-8')

    url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
    recvd = requests.get(url)

    locations = re.findall(r'<location wl_ver="3">.+?</location>',
                           recvd.text,
                           re.DOTALL)
    kmaData = ''
    for loc in locations:
        prov = re.findall(r'<province>(.+)</province>', loc)
        city = re.findall(r'<city>(.+)</city>', loc)
        # print(prov[0], city[0])
        # f.write(prov[0] + ',' + city[0] + '\n') # csv 파일 형태 : ',' 로 구분
        kmaData += prov[0] + ',' + city[0] + '\n'

        data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)

        for datum in data:
            item = re.findall(r'<.+?>(.+?)</.+?>',
                              datum, re.DOTALL)
            # print(item)
            # f.write(str(item) + '\n')  # 문자열만 write 가능
            # kmaData += str(item) + '\n'

            # f.write(item[0] + ',' +
            #         item[1] + ',' +
            #         item[2] + ',' +
            #         item[3] + ',' +
            #         item[4] + ',' +
            #         item[5] + '\n')
            kmaData += (item[0] + ',' +
                        item[1] + ',' +
                        item[2] + ',' +
                        item[3] + ',' +
                        item[4] + ',' +
                        item[5] + '\n')

    f.write(kmaData)

    f.close()
write2('Data/kma.txt')

print('5','#'*30)
def write3(filename):
    f = open(filename, 'w', encoding='utf-8')

    url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
    recvd = requests.get(url)

    locations = re.findall(r'<location wl_ver="3">.+?</location>',
                           recvd.text,
                           re.DOTALL)
    kmaData = ''
    for loc in locations:
        prov = re.findall(r'<province>(.+)</province>', loc)
        city = re.findall(r'<city>(.+)</city>', loc)
        # kmaData += prov[0] + ',' + city[0] + '\n'

        data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)

        for datum in data:
            item = re.findall(r'<.+?>(.+?)</.+?>',
                              datum, re.DOTALL)
            kmaData += (prov[0] + ',' +  # 모든 데이터에 공유 값 붙임
                        city[0] + ',' +
                        item[0] + ',' +
                        item[1] + ',' +
                        item[2] + ',' +
                        item[3] + ',' +
                        item[4] + ',' +
                        item[5] + '\n')  # 전형적인 csv 형태
    f.write(kmaData)

    f.close()
write3('Data/kma2.txt')

a, b = 3.141592, 'hello'
print(a, b)

t = '{} {}'.format(a, b) # 형식 지정 저장
print(t) # 3.141592 hello

print('{0} {1}'.format(a, b))         # 3.141592 hello
print('{1} {0}'.format(a, b))         # hello 3.141592
print('{1} {0} {0} {1}'.format(a, b)) # hello 3.141592 3.141592 hello

print('[{0:10}] [{1:10}]'.format(a, b))               # 고정길이 지정 [  3.141592] [hello     ]
print('[{0:<10}] [{1:^10}] [{1:>10}]'.format(a, b))   # 정렬 지정 [3.141592  ] [  hello   ] [     hello]

print('[{:10.2}]'.format(a))      # 소수점 지정 [       3.1]
print('[{:10.2f}]'.format(a))     # 소수점 지정 [      3.14]












