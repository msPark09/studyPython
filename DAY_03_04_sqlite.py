# DAY_03_04_sqlite

# file 단위의 dbsystem

import DAY_03_03_csv

print(__name__) # DAY_03_03_csv : 다른 파일에 포함되었을 때(java 객체같이)
                # __main__      : 실행되는 파일 - 현 실행 파일 (java main같이)
# rows = DAY_03_03_csv.read_kma_txt('Data/kma2.txt')
# print(rows)

import sqlite3

def create_table():
    conn = sqlite3.connect('Data/kma.sqlite')
    cur = conn.cursor()

    query = 'CREATE TABLE KMA (PROV TEXT, CITY TEXT, MODE TEXT, TMEF TEXT, WF TEXT, TMN TEXT, TMX TEXT, RELI TEXT)'
    cur.execute(query)

    conn.commit()
    conn.close()


def insert_table(row):
    conn = sqlite3.connect('Data/kma.sqlite')
    cur = conn.cursor()

    base = 'INSERT INTO KMA VALUES("{}","{}","{}","{}","{}","{}","{}","{}")'
    query = base.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
    cur.execute(query)

    conn.commit()
    conn.close()

def insert_all(rows):
    conn = sqlite3.connect('Data/kma.sqlite')
    cur = conn.cursor()

    base = 'INSERT INTO KMA VALUES("{}","{}","{}","{}","{}","{}","{}","{}")'
    for row in rows:  # 모든 데이터 입력됨
        query = base.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        cur.execute(query)

    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect('Data/kma.sqlite')
    cur = conn.cursor()

    query = 'SELECT * FROM KMA'
    result = cur.execute(query)

    for row in result:
        print(row)

    conn.commit()
    conn.close()

    return result


# 문제
# city가 부산인 데이터만 가져와 보세요.
def search_all(city):
    conn = sqlite3.connect('Data/kma.sqlite')
    cur = conn.cursor()

    # query = 'SELECT * FROM KMA WHERE CITY = "'+city+'"'

    # base = 'SELECT * FROM KMA WHERE CITY = "{}"'
    # query = base.format(city)

    query = 'SELECT * FROM KMA WHERE CITY = "{}"'.format(city)
    results = list(cur.execute(query))

    # for row in result:
    #     print(row)

    # conn.commit()
    conn.close()

    return results

if __name__ == '__main__':
    # create_table() # 테이블 생성

    # for row in rows:
    #     insert_table(row)

    # insert_all(rows)

    # fetch_all()

    rows = search_all('부산')
    print(*rows, sep='\n')















