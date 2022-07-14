# chapter 8-1
"""
함수
def 함수명(매개변수):
    실행문1
    실행문2
    return 반환하는 값
실행문
함수명(전달인자)
"""
from re import I


def printHello():         # 함수 정의
    print("Hello")        # 함수 내용
printHello()              # 함수 실행

# chapter 8-2
# 매개변수가 있는 함수
def printSum(a, b): 
    print(a + b)
printSum(3, 4)
printSum(5, 9)
x = int(input("숫자를 입력하시오.:"))
y = int(input("숫자를 하나 더 입력하시오.:"))
printSum(x, y)

# chapter 8-3
# 반환값이 있는 함수
def getSum(a, b):
    sum = a + b
    return sum
result = getSum(6, 5)
print(result)

# chapter 8-4
# 함수 안에서 정의해준 변수는 지역변수로 코드전체에서 사용할수 없다.

# chapter 8-5
"""
내장 함수
input()  입력
print()  출력
abs()    절대값
변수이름을 내장함수 이름으로 정의하지 않는것이 좋음
"""
number = -10
print(number)
abs_number = abs(number)
print(abs_number)
print(abs(number))
#  예약어 - 변수이름을 예약어로 정의 할 수 없다.

# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter1 난이도 하 프로젝트 - 1-9 정수 n까지의 합을 구하는 함수 만들기
def numSum(n):
    result = 0
    for i in range(0, n+1):
        result = result + i
    print("0부터", n ,"까지의 합계는", result ,"입니다.")
x = int(input("정수를 입력하세요.:"))
numSum(x)

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter2 난이도 중 프로젝트 - 2-7 도형별 넓이 계산기
print(
"""==========도형목록==========
1. 원
2. 삼각형
3. 직사각형
4. 정사각형""")
def circle(radius):
    circle_area = radius * radius *3.1415
    print("반지름이", str(radius)+"인 원의 넓이는 약", str(circle_area)+"입니다.")
def triangle(width, height):
    triangle_area = (width * height) / 2
    print("밑변이", str(width)+"이고 높이가", str(height)+"인 삼각형의 넓이는", str(triangle_area)+"입니다.")
def square(Width, Height):
    square_area = Width * Height
    print("가로가", str(Width)+"이고 세로가", str(Height)+"인 직사각형의 넓이는", str(square_area)+"입니다.")
def asquare(hanbyun):
    asquare_area = hanbyun * hanbyun
    print("한 변의 길이가", str(hanbyun)+"인 정사각형의 넓이는 약", str(asquare_area)+"입니다.")
num = int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해 주세요.:")) 
if num == 1:
    a = float(input("원의 반지름 길이를 입력해 주세요.:"))
    circle(a)
elif num == 2:
    x = float(input("삼각형의 밑변의 길이를 입력해 주세요.:"))
    y = float(input("삼각형의 높이의 길이를 입력해 주세요.:"))
    triangle(x, y)
elif num == 3:
    p = float(input("직사각형의 가로의 길이를 입력해 주세요.:"))
    q = float(input("직사각형의 세로의 길이를 입력해 주세요.:"))
    triangle(p, q)
elif num == 4:
    z = float(input("정사각형의 한 변의 길이를 입력해 주세요.:"))
    asquare(z)
else:
    print("번호를 잘 못 입력하였습니다.")

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter2 난이도 중 프로젝트 - 2-11 함수를 활용한 구구단
def gugudan(x):
    for i in range (1, 10):
        result = i * x
        print(i,"x",x,"=",result)
while True:
    num = int(input("2부터 9 사이 숫자를 입력해 주세요. (1을 누르면 프로그램이 종료됩니다.)"))
    if num == 1:
        print("프로그램을 종료합니다.")
        break
    elif 2 <= num <= 9:
        gugudan(num)
    else:
        print("범위 외의 숫자입니다. 다시 시도하세요.")
    
# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter2 난이도 중 프로젝트 - 2-13 최댓값의 위치
def where_max(num):
    temp_max = 0

    for i in range(1, len(num)):
        if num[i] > num[temp_max]:
            temp_max = i 
    return temp_max
lst = [10, 55, 66, 81, 10, 50, 78]
print(where_max(lst))