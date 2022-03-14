# from random import *
# date = randint(4, 28)
# print(f'오프라인 스터디 모임 날짜는 매월 {date}일로 선정되었습니다.')


# adr = "http://youtube.com"
# num = adr[7:adr.index(".")]
# a = num[:3]
# b = str(len(num))
# c = str(num.count('e'))
# abc = a+b+c

# print("생성된 비밀번호 : " + abc + "!")


from random import *
id = list(range(1, 21))
shuffle(id)
chi = id.pop()
coffee = sorted(sample(id, 3))
print(" -- 당첨자 발표 --")
print(f'치킨 당첨자 : {chi}')
print(f'커피 당첨자 : {coffee}')
print(' -- 축하합니다 --')