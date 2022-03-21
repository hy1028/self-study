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


# from random import *
# id = list(range(1, 21))
# shuffle(id)
# chi = id.pop()
# coffee = sorted(sample(id, 3))
# print(" -- 당첨자 발표 --")
# print(f'치킨 당첨자 : {chi}')
# print(f'커피 당첨자 : {coffee}')
# print(' -- 축하합니다 --')

# students = [1, 2, 3, 4, 5]
# students1 = [i + 100 for i in students]
# print(students1)

# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)


# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# from random import *
# count = 0
# for i in range(1, 51):
#     time = randint(5, 50)
#     if time >= 5 and time <= 15:
#         count += 1
#         print(f'[O] {i}번째 손님 (소요시간 : {time}분)')
#     else:
#         print(f'[ ] {i}번째 손님 (소요시간 : {time}분)')
# print(f'총 탑승 승객 : {count} 분')


# def std_weight(height, gender):
#     if gender == "남자":
#         result = format(height/100 * height/100 * 22, '.2f')
#     else:
#         result = format(height/100 * height/100 * 21, '.2f')
#     print(f'키 {height}cm {gender}의 표준 체중은 {result}kg 입니다.')

# std_weight(175, "남자")


#print(f'{500:_>10}')

#print(f'{100000000000:^<+30,}')

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50")
# score_file.close()

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# import pickle
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()


# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# for i in range(1, 11):
#     file = open(f'{i}주차.txt', "w", encoding="utf8")
#     file.write(f'- {i} 주차 주간보고 -')
#     file.write('\n부서 :')
#     file.write('\n이름 :')
#     file.write('\n업무 요약 :')
#     file.close()

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

class AttackUnit(Unit):
        def __init__(self, name, hp, speed, damage):
            Unit.__init__(self, name, hp, speed)
            self.damage = damage

        def attack(self, location):
            print(f'{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]')

        def damaged(self, damage):
            print(f'{self.name} : {damage} 데미지를 입었습니다.')
            self.hp -= damage
            print(f'{self.name} : 현재 체력은 {self.hp} 입니다.')
            if self.hp <= 0:
                print(f'{self.name} : 파괴되었습니다.')

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print(f'{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]')

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print('[공중 유닛 이동]')
        self.fly(self.name, location)


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")