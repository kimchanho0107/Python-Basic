# chapter 14-1
# chapter 14-2
# chapter 14-3
# 오늘의 과제: Part2 변수와 함께 만드는 나의 첫 포트폴리오 - chapter1 난이도 하 프로젝트 - 1-13 할인된 가격을 알려주는 계산기 클래스 만들기
class Calculator:
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount
    def getResult(self):
        return self.price - (self.price*self.discount/100)
price = int(input("원가를 입력하세요.:"))
discount = int(input("몇 퍼센트 할인하나요?:"))
calculator = Calculator(price, discount)
print("최종 금액은", calculator.getResult(),"입니다.")