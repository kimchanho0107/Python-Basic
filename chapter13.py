# chapter 13-1
# 딕셔너리
dic = {"python":"파이썬","c":"c언어","java":"자바"}
dic2 = {"int":1,"str":"문자","list":[1,2],"tuple":(1,2),"dict":{"python":"파이썬"}}
print(dic2["int"])
print(dic2["str"])
print(dic2["list"])
print(dic2["tuple"])
print(dic2["dict"])

# chapter 13-2
# 딕셔너리 수정하기
# 1. key, value 한 쌍 추가하기
dic["html"] = "웹프로그래밍"
print(dic)
# 2. key, value 여러 쌍 추가하기 : update()
dic.update({"CSS":"css",'JavaScript':'JS'})
print(dic)
# 3. key, value 쌍 삭제하기 : del
del dic["c"]
print(dic)
# 4. value 값 수정하기
dic["python"] = "파이떤"
print(dic)

# chapter 13-3
# for문과 딕셔너리
# 딕셔너리의 key값으로 반복하기
print(dic.keys())
for i in dic.keys():
    print(i, end=" ")
    print(dic[i], end=" ")
# 딕셔너리의 value값으로 반복하기
print(dic.values())
# 딕셔너리의 key, value 쌍으로 반복하기
print(dic.items())

# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter1 난이도 하 프로젝트 - 1-12 튜플과 딕셔너리로 문자열 길이 출력하기
myTuple = ("hello","this is python","ok,bye~")
myDictionary = {}
for i in myTuple:
    myDictionary[i] = len(i)
print(myDictionary)


# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter3 난이도 상 프로젝트 - 3-7 음료수 자판기



# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter3 난이도 상 프로젝트 - 3-11 영화 예매 프로그램 만들기