# chapter 11-1
# 튜플
a = (1, 2)
print(a)
print(type(a))

# chapter 11-2
"""
튜플의 특징
1. 괄호 사용
2. 한번 선언한 값을 바꿀 수 없음
3. 괄호 생략 가능
4. 변하지 않는 값일 경우 사용
"""

# chapter 11-3
# 튜플 활용
a = 10
b = 20
c,d = a, b
print(a, b, c, d)

# 튜플의 최대 최솟값 구하기
def minmax(ex_lst):
    return min(ex_lst), max(ex_lst)

a = [1, 2, 3, 4, 5]
result = minmax(a)
print(result)
print(type(result))

# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter3 난이도 상 프로젝트 - 3-6 뒤집은 소수
def reverse(x):
    x = list(str(x))
    x.reverse()
    rx = ''.join(x)
    return int(rx)
def is_prime(x):
    for i in range(2, x+1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
    return prime

num = int(input("입력받을 숫자의 개수를 입력해 주세요.:"))
lst = []
for i in range(num):
    temp = int(input("%d번째 숫자를 입력해 주세요:" % (i + 1)))
    lst.append(temp)
for i in lst:
    if is_prime(reverse(i)):
        print(i, end=" ")