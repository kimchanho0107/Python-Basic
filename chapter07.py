# chapter 7-1
# 반복문이 필요할때 0부터 9까지 출력
for i in range(10):
    print(i)

# chapter 7-2
""" 
반복문에서 반복할 구간 설정하는 방법
range(끝나는 숫자)
range(시작 숫자, 끝나는 숫자)
range(시작 숫자, 끝나는 숫자, 간격)
"""
for a in range(1,10):
    print(a)
for b in range(0,10,2):
    print(b)
# 숫자를 줄어 들게 하고싶을때는 간격을 음수로 하면됨
for c in range(10,0,-1):
    print(c)
# 변수를 사용한 for문
x = 3
for d in range(1,x+1):
    print(d)

# chapter 7-3
# 중첩 for 문
"""
i가 2일때 j가 1~9인값 계산
            ~
i가 9일때 j가 1~9인값 계산
"""
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end="")
    print()          # 줄바꿈


# chapter 7-4
# for문
for x in range(1, 4):
    print(x)
"""
while문
while 조건식:
    실행문
"""
y = 1
while y <= 3:
    print(y)
    y = y + 1
 
# chapter 7-5
# 반복문 속 조건문과 break
number = 0           # 변수 초기화
while True:
    number = int(input("문을 여시겠습니까? (1:Yes / 2:No)")) 
    if number == 1:
        print("문이 열렸습니다.")
        break
    elif number == 2:
        print("문을 열 수 없습니다.")

# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter1 난이도 하 프로젝트 - 1-8 짝수이면서 7의 배수는 아닌 수 찾기
count = 0
for num in range (1,101):
    if num % 2 == 0:
        if num % 7 != 0:
            count = count + 1
        else:
            count = count
    else:
        count = count
print(count)

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter2 난이도 중 프로젝트 - 2-4 높이가 n인 직각이등변삼각형 만들기
height = int(input("삼각형의 높이를 입력해 주세요.:"))  # 높이를 입력받아 정수형으로 저장
for i in range(1,height + 1):                         # for문 범위 1부터 (높이+1)
    print(" "*(height-i)+"*"*i)

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter2 난이도 중 프로젝트 - 2-5 팩토리얼 계산하기
num = int(input("숫자를 입력해 주세요.:"))
n = 1
total = 1
while n <= num:
    total = total * n
    n = n + 1
print(total)

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter2 난이도 중 프로젝트 - 2-12 소인수분해
num = int(input("숫자를 입력해 주세요.:"))
d = 2
while d <= num:
    if num % d == 0:
        print(d, end=" ")
        num /= d
    else:
        d = d + 1

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter3 난이도 상 프로젝트 - 3-3 8월 달력 출력하기 


# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter3 난이도 상 프로젝트 - 3-8 BMI 전자레인지 시간 설정하기 