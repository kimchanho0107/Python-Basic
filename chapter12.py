# chapter 12-1
"""
집합 만들기 -  중복 허용x(리스트나 튜플의 중복값을 제거하려고할때 집합 사용), 순서가 없음 // 
set()함수, 
"""
a = set([1,2,3,4,5])
b = set("apple")
c = {3, 6, 4, 7, 1, 7}
print(a, type(a))
print(b, type(b))
print(c, type(c))

# chapter 12-2
x = set([1,2,3])
y = set([2,3,4])
# 합집합 | 또는 union()
print(x|y)
print(x.union(y))
print(y.union(x))
# 교집합 & 또는 intersection()
print(x&y)
print(x.intersection(y))
print(y.intersection(x))
# 차집합 - 또는 difference()
print(x|y)
print(x.difference(y))
print(y.difference(x))

# chapter 12-3
# 집합 응용 함수
z = set([1,2,3,4,5])
# 데이터 1개 추가하기 - add()
z.add(-1)
print(z)
# 데이터 여러개 추가하기 - update()
z.update([1,2,3,4,5,6,7,8])
print(z)
# 원하는 값을 찾아 삭제하기 - remove()
z.remove(1)
print(z)


# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter2 난이도 중 프로젝트 - 2-2 문장 내 단어 오름차순으로 출력하기
q = input("문장을 입력해 주세요.:")
t = q.split(" ")
t = set(t)
t = list(t)
t.sort()
for i in t:
    print(i, end=" ")