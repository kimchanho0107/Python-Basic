# 4-1
"""
산술 연산자 + - * / %
대입 연산자 = += -=
관계 연산자 < > != ==
논리 연산자 and or not
"""

# 4-2
# 기본 사칙연산
print(200-10+100)
print(10*10)
print(100/5)
print(100%3)
# 변수를 이용한 사칙연산
a = 10
b = 20
c = a*b
print(c)
print(a-b)

# 4-3
# 나눗셈 /
print(55/3)
# 몫을 구하는 버림 나눗셈 //
print(55//3)
# 나머지를 구하는 나눗셈 %
print(55%3)
# 거듭제곱 **
print(2**4)
print(2**10)

# 4-4
# 구구단 5단 만들기
a = 5
print(a,"* 1 =",a*1)
print(a,"* 2 =",a*2)
print(a,"* 3 =",a*3)
print(a,"* 4 =",a*4)
print(a,"* 5 =",a*5)
print(a,"* 6 =",a*6)
print(a,"* 7 =",a*7)
print(a,"* 8 =",a*8)
print(a,"* 9 =",a*9)
""" 
홀짝 확인 프로그램
값을 2로 나눈 나머지(%)가 1이면 홀수, 0이면 짝수
"""
a = 7
b = 4732
print("a의 나머지는",a%2,"입니다")
print("b의 나머지는",b%2,"입니다")

# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter1 난이도 하 프로젝트 - 1-4 어떻게 돈을 내야 할까?
money = 8970
a = money // 1000
b = (money%1000)// 100
c = (money%100) // 10
print(money,"원을 지불하려면")
print('1000원 지폐',a,'장')
print('100원 동전',b,'장')
print('10원 동전',c,'장이 필요합니다.')

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter2 난이도 하 프로젝트 - 2-14 시간 변환 계산기
time = int(input("시간(초)를 입력하시오.:"))   # 시간 입력
print(str(time)+"초는 ", end='')              # (입력한 시간)는
if time >= 86400:                             # 입력한 시간이 86400초(1일)보다 클때 계산
    temp = time // 86400                      # temp 변수에 입력한 시간을 1일로 나눈 몫을 저장
    time = time - (temp*86400)                # time 변수에 (처음 입력된 시간)-(일수로 빠진 값)한 값 저장
    print(str(temp)+"일", end="")
if time >= 3600:                              # time 변수의 값이 3600초(1시간)보다 클때 계산
    temp = time // 3600                       # temp 변수에 입력한 시간을 1시간으로 나눈 몫을 저장
    time = time - (temp*3600)                 # time 변수에 (처음 입력된 시간)-(시간수로 빠진 값)한 값 저장
    print(str(temp)+"시간", end="")
if time >= 60:                                # time 변수의 값이 60초(1분)보다 클때 계산
    temp = time // 60                         # temp 변수에 입력한 시간을 1분으로 나눈 몫을 저장
    time = time - (temp*60)                   # time 변수에 (처음 입력된 시간)-(분수로 빠진 값)한 값 저장
    print(str(temp)+"분", end="")
if time != 0:                                 # time 변수의 값이 0이 아닐때 time의 값 출력
    print(str(time)+"초입니다.", end="")
else:                                         # time 변수의 값이 0일때 '입니다.' 출력
    print("입니다.")


