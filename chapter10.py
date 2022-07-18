# chapter 10-1
"""
리스트 생성하기
리스트이름 = [0번째 인덱스, 1번째, 2번째, ....]
"""
list = ["My", 'age', 'is', 20]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
# 인덱스 값 재저장
list[3] = 23
print(list[3])

# chapter 10-2
for x in list:
    print(x)
for i in range(len(list)):
    print("인덱스",i,"값:",list[i])
for a in range(len(list)):
    list[a] = "change"
print(list)

# chapter 10-3
""" 
리스트 슬라이싱
리스트이름[시작번호 : 끝번호+1]
"""

# chapter 10-4
"""
리스트 응용 함수
리스트.append(데이터)              : f리스트에 데이터 삽입
리스트.insert(데이터)              : 리스트의 원하는 인덱스에 데이터 삽입
del. 리스트[삭제할 값의 인덱스]     : 인덱스로 데이터 삭제
리스트.remove(데이터)              : 원하는 값을 찾아 삭제
리스트.sort(데이터)                : 리스트 정렬
리스트.reverse(데이터)             :리스트의 인덱스를 거꾸로
"""

# chapter 10-5
# 2차원 리스트
list2d = [["이","차","원"],["리","스","트"]]

# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter1 난이도 하 프로젝트 - 1-11 입력받은 수의 평균 구하기
numlist = []
total = 0
for i in range(0, 7):
    numlist.append(int(input("정수를 입력하세요.:")))
    total = total + numlist[i]
print("평균 :", total / 7)