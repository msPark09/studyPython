# DAY_04_01_exception
from logging import exception


def not_used():
    def validate(n):
        '''
        데이터의 유효성 검사
        :param n: 정수
        :return: 사용할 수 있으면 True, 아니면 False
        '''
        if n < 0:
            return False
        return True

        if n == 0:
            raise ValueError # raise : exception 발생시킴

    # help(validate) # 함수 정의 확인

    n = int(input())

    if validate(n):
        print('Pass')
    else:
        print('Fail')

try:
    # a = input()
    a = 123
    a = int(a)
    print(a + 3)
# except TypeError:
#     print('TypeError')
# except ValueError:
#     print('ValueError')
except:              # exception 발생
    print('unknown')
else:                # exception 미발생
    print('else')
finally:
    print('finally')

print('='*30)

# 문제
# 아래 코드에서 발생하는 예외를 처리해 주세요.
try:
    a =[1,3,5]
    size = len(a)
    print(a[size])
except IndexError as e:
    print('IndexError : ', e) # error 내용

# 문제
# 정수 1개를 입력 받아서 반환하는 함수를 만드세요.
def retunA():
    try:
        a = input()
        a = int(a)
    except ValueError as e:
        print('ValueError : ', e)
    else:
        return a

ra = retunA()
print(ra)

# True 일때 까지 계속 입력되도록 하는 함수
def get_one():
    while True:
        try:
            a = input()
            a = int(a)
            break
        except ValueError:
            print('wrong')

    return a

ra = get_one()
print(ra)


for i in range(5):
    if i == 2:
        break  # 중간탈출시 else 넘어감
    print(i)
else:          # 중간 탈출 없이 모든 range 끝 후에 수행
    print('else')

