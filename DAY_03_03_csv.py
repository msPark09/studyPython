# DAY_03_03_csv

# 문제
# 나머지 코드를 만들어 보세요.
def read_kma_txt(filename):
    f = open(filename, 'r', encoding='utf-8')
    rows=[]
    for line in f :
        line = line.strip()
        # print(line.split(','))
        rows.append(line.split(','))
    f.close()
    return rows

# rrows = read_kma_txt('Data/kma2.txt')
# print(rrows)
# print(*rrows, sep='\n')

# 문제
# read_kma_txt 함수가 반환하는 값을 반복문을 사용해서 출력해 주세요.

def print_kma(rows):
    for row in rows:
        for col in row:
            print(col, end=',')
        print()

# print_kma(rrows)

import csv
def read_us500(filename):
    f = open(filename, 'r', encoding='utf-8')

    #skip header
    f.readline() # => 한줄 읽고 저장하지 않으니 헤더 제거(reader pointer 이동)

    rows =[]
    for line in csv.reader(f):
        rows.append(line)

    f.close()
    # rows.pop(0)
    return rows

# print(*rrows, sep='\n')

def write_kma(filename, rows):
    f = open(filename,'w',encoding='utf-8', newline='')
    # writer = csv.writer(f)
    # for row in rows:
    #     writer.writerow(row) # list로 입력

    # csv.writer(f).writerows(rows)      # delimiter=',' defualt
    csv.writer(f,
               delimiter=':',          # 구분자 변경 가능
               quoting=csv.QUOTE_ALL # 데이터를 앞뒤로 감싸는 문자
               ).writerows(rows)

    f.close()

# print(__name__)
if __name__ == '__main__': # 다른 파일에서 import시 사용 방지
    print(__name__)
    rrows = read_us500('Data/us-500.csv')
    write_kma('Data/kma3.csv', rrows)



























