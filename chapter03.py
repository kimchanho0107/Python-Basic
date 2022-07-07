# chapter 3-1
# 변수 name에 Chanho를 저장, 변수 age에 23을 저장함
name = "Chanho"
age = 23
# 변수에 저장된 값을 출력할 때는 따옴표를 쓰지 않음
print("name")
print(name)
# 변수에 다른 값을 덮어씌우기가 가능함
food = "pizza"
print(food)
food = "cake"
print(food)
food = "hamburger"
print(food)
# 값이 저장된 변수를 다른 변수에 저장할 수 있음
a = 10
b = a
print(b)

# chapter 3-2
# 자료형의 종유로는 문자열(str), 숫자(int, float), 불(bool), 리스트(list), 튜플(tuple), 딕셔너리(dict), 집합 등이 있음
print(type("문자열"))  # 문자열(str)
print(type(10))  # 정수(int)
print(type("10"))  # 문자열(str)
print(type(2.5))   # 실수(float)
print(type(True))   # 불(bool)
print(type([3,5,7]))  # 리스트(list)
print(type((1,2,3)))  # 튜플(tuple)
print(type({'name':'chanho'}))  # 딕셔너리(dict)



# chapter 3-3
# 숫자 자료형은 정수(int), 정수(float) 등이 있음
print(type(10))   # 정수(int)
print(type(0))    # 정수(int)
print(type(-7))   # 정수(int)
print(type(2.5))  # 정수(float)
# 숫자 자료형과 문자열 자료형의 합, 따옴표 안에는 값은 문자열 자료형으로 취급됨
print(2000+23) # 숫자 자료형 + 숫자 자료형
print("2000"+"23")  # 문자열 자료형 + 문자열 자료형
print(0.5+0.5) # 숫자 자료형 + 숫자 자료형
print("0.5"+"0.5") # 문자열 자료형 + 문자열 자료형

# chapter 3-4
# 불 자료형은 참(true), 거짓(false)가 있음
print(6>2) # 참(true)
print(1>8) # 거짓(false)
# 참(true), 거짓(false)의 자료형 출력
print(type(True))
print(type(False))


# chapter 3-5
"""
변수 이름 규칙
1. 숫자로 시작할 수 없다. ex) 2name = chanho
2. 변수 이름에 공백이 있으면 안된다. ex) what is your name = chanho
  -공백을 사용하고 싶다면 언더바(_)를 사용함
3. 예약어를 변수 이름으로 사용할 수 없다. ex) True = chaho
"""

# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter1 난이도 하 프로젝트 - 1-3 자료형 마스터!
my_name = "KimChanho"
age = 23
weight = 72.3
army = True
print(type(my_name))
print(type(age))
print(type(weight))
print(type(army))




