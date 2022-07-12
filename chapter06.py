# chapter 6-1
"""
if문의 기본 구조

if 조건식1:
    실행문1
else:
    실행문2
"""

# chapter 6-2
"""
비교 연산자
>  크다
<  작다
>=  크거나 같다
<=  작거나 같다
==  같다
!=  아니다
"""
a = 50
b = 7
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

# chapter 6-3
"""
논리 연산자
and : 모두 참일 떄만 참
or  : 하나 이상이 참일 때 참
not : 값의 반대
"""

# chapter 6-4
money = 60000
if money >= 5000:                         # if, else 문은 들여쓰기를 해야함
    print("결제가 가능합니다.")
else:
    print("결제가 불가능합니다.")
print("다른 카드를 준비해 주세요.")         # 들여쓰기를 하지 않은 문장은 조건문에 포함되지 않음


# chapter 6-5
# if, else 조건 이외에 조건을 더 추가로 쓰고 싶다면 elif문을 사용
button =  int(input("1~3 중에서 입력하시오.:"))
if button == 1:
    print("한식")
elif button == 2:
    print("중식")
elif button == 3:
    print("일식")
else :
    print("숫자를 잘 못 입력하였습니다.")

# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter1 난이도 하 프로젝트 - 1-6 합격과 불합격 통보하기
first = float(input("첫번째 과목의 점수를 입력하세요.:"))
second = float(input("두번째 과목의 점수를 입력하세요.:"))
third = float(input("세번째 과목의 점수를 입력하세요.:"))
average = (first + second + third) / 3
if average >= 50:
    print("평균 점수는", str(average)+"점으로 합격입니다.")
else :
    print("평균 점수는", str(average)+"점으로 불합격입니다.")

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter1 난이도 하 프로젝트 - 1-7 BMI 결과보기 
height = float(input("키를 입력하세요.:"))
weight = float(input("몸무게를 입력하세요.:"))
mheight = height*0.01
BMI = weight / (mheight*mheight)
if BMI >= 25:
    print("BMI 지수가",str(BMI)+"이므로 비만입니다.")
elif 25 >BMI >= 23:
    print("BMI 지수가",str(BMI)+"이므로 과체중입니다.")
elif 23 > BMI >= 18.5:
    print("BMI 지수가",str(BMI)+"이므로 정상체중입니다.")
else :
    print("BMI 지수가",str(BMI)+"이므로 저체중입니다.")

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter2 난이도 중 프로젝트 - 2-1 윤년 판단하기
year = int(input ("연도를 입력하세요.:"))
if (year % 4 == 0 and year % 100 != 0) :
    print(year,"은 윤년입니다.")
elif (year % 400 == 0) :
    print(year,"은 윤년입니다.")
else :
    print(year,"은 윤년이 아닙니다.")
    

