# class Unit:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#     def attack(self):
#         print(self.name, "이(가) 공격을 수행합니다. [전투력:", self.power,"]")
#
# class Monster(Unit):
#     def __init__(self, name, power, type):
#         self.name = name
#         self.power = power
#         self.type = type
#
# monster = Monster("슬라임", 10, "초급")
# monster.attack()


# dict = {}
# dict['안녕'] = 'Hello'
# dict['기적'] = 'Miracle'
# dict['노력'] = 'effort'
#
# dict['안녕'] = 'Hi'
#
# print(sorted(dict))
# print(sorted(dict, reverse=True))
# print(sorted(dict.values()))

# for i, k in enumerate(dict):
#     print("[인덱스", i, "] 한글:", k, "/ 영어:", dict[k])


# user_input = int(input('정수를 입력하세요: '))
# print("제곱 :", user_input ** 2)

# # bin(), hex() : 10진수 -> 2진수, 10진수 -> 16진수 변환
# print(bin(128))
# print(hex(230))
#
# #다시 10진수로 바꿀 땐 int() 함수 이용
# print(int('0b10000000', 2))
# print(int('0xe6', 16))

# str = "Hello World"
# print(str[::-1])

# isalpah() : 특정한 문자열이 문자로만 이루어져 있는지 확인, 숫자나 공백 안됨
# isdigit() : 특정한 문자열이 숫자로만 이루어져 있는지 확인
# isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
#
# my_function = lambda a, b: a + b
# result = list(map(my_function, list1, list2))
# print(result)


















