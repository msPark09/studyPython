# DAY_04_06_comprehension

# 반복문을 이용한 list 생성
# comprehension : 한줄 반복문을 사용하여 리스트 생성
import random
random.seed(1)

print([i for i in range(5)]) # [0, 1, 2, 3, 4]
print([-1 for _ in range(5)]) # [-1, -1, -1, -1, -1]

# for i in range(5):
#     if i % 2 == 0:
#         i

a = [random.randrange(100) for _ in range(10)]
print(a)

# 문제
# 리스트에서 홀수만 출력해 보세요
print([i for i in a if i%2 != 0])
print([i for i in a if i%2])     # 0 외의 숫자 True
# 짝수만 거꾸로 출력해 보세요
print([i for i in a[::-1] if i%2 == 0])
print([i for i in a[::-1] if not i%2])

# 활용
print(sum([i for i in a if i%2]))
print(max([i for i in a if i%2]))

print('='*30)

a1 = [random.randrange(100) for _ in range(10)]
a2 = [random.randrange(100) for _ in range(10)]
a3 = [random.randrange(100) for _ in range(10)]

b=[a1,a2,a3]
print(*b, sep='\n')

# 문제
# 리스트의 전체 합계를 구하세요
# print(sum(j for j in [sum(i) for i in b]))
print(sum([sum(i) for i in b])) # sum(list) 리스트 합계 구하기

# 리스트를 거꾸로 출력해 보세요.
print(*[i for i in b[::-1]], sep='\n')
print(*[i[::-1] for i in b[::-1]], sep='\n')
print(*[[j for j in i[::-1]] for i in b[::-1]], sep='\n')

print([j for i in b for j in i])
print([j for i in b for j in i if j % 2])



















