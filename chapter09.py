# chapter 9-1
# 문자열 인덱싱 - 문자열의 글자에 번호를 지정하고 가리키는 것 (0부터 시작, 띄어쓰기기호도 포함)
hi = "파이썬 공부는 즐거워!"
print(hi[2])
print(hi[6])
# 슬라이싱을 음수로하면 거꾸로감
print(hi[-1])
print(hi[-10])
# 문자열 슬라이싱 - 원하는 위치부터 위치까지 문자열을 자르는 것
# 변수명[시작번호 : 끝번호+1]
# 변수명[시작번호 : ] - 시작번호부터 끝까지
# 변수명[ : 끝번호+1] - 시작번호부터 끝번호까지
print(hi[4 : 7])
print(hi[7 : 10])
# 변수명[시작번호 : 끝번호+1 : 간격] - 간격만큼 인덱스를 건너뛰며 슬라이싱

# chapter 9-2
"""
문자열 포매팅1 - 문자열 포멧코드 사용
정수%d 실수%f 문자열%s  -  %변수명 or %(변수명, 변수명 )
"""
name = "김찬호"
age = 23
print("내 이름은 %s, %d살 이다" %(name, age))

"""
문자열 포매팅2 - format 함수 사용
print("{0}{1}" .format({0}에 대입할 변수이름, {1}에 대입할 변수이름))
"""
print("내 이름은 {0}, {1}살 이다" .format(name, age))

"""
문자열 포매팅3 - f 문자열 사용하기
print(f"{변수이름}")
"""
a = 15
print(f"a는{a}")

# chapter 9-3
word = "apple"
# len() - 문자열 길이 구하기
print(len(word))
# count() - 특정 문자의 개수 세기
print(word.count("p"))
# find() - 특정 문자의 위치 찾기
print(word.find("l"))
# replace() - 특정 문자열을 다른 문자열로 변환하기
print(word.replace("apple","banna"))
# split() - 특정 문자를 기준으로 문자열 자르기
word1 = "apple is red"
print(word1.split())
"""
join() - 문자열 사이에 문자열을 삽입하기
upper() - 소문자를 대문자로 바꾸기
lower() - 대문자를 소문자로 바꾸기
strip() - 양쪽 공백 지우기
"""

# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter1 난이도 하 프로젝트 - 1-10 이름 출력하기
my_name = "제 이름은 김찬호입니다."
print(my_name[6:9])

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter3 난이도 상 프로젝트 - 3-1 영어 문장 대소문자 올바르게 사용하기
sentence = input("문장을 입력해 주세요.:")
sentence = sentence.lower().split(".")
answer = []
for s in sentence:
    s = s.capitalize()
    if s in "i'":
        s = s.replace("i'","I'")
        answer.append(s)
    elif s in " i ":
        s = s.replace(" i "," I ")
        answer.append(s)
    elif s in "i ":
        s = s.replace("i ","I ")
        answer.append(s)
    elif s in " i":
        s = s.replace(" i"," I")
        answer.append(s)
    else:
        answer.append(s)
print(".".join(answer))


# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter3 난이도 상 프로젝트 - 3-2 자릿수의 합이 가장 큰 수 찾기

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter3 난이도 상 프로젝트 - 3-4 두 숫자 사이의 n의 배수 찾기

# 선택 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter3 난이도 상 프로젝트 - 3-9 가운데 글자 찾기

