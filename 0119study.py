### 파이썬 300제 241번
##import datetime
##
##now = datetime.datetime.now()
##print(now)

### 파이썬 300제 242
##import datetime
##
##now = datetime.datetime.now()
##print(type(now))

### 파이썬 300제 243
##import datetime
##
##now = datetime.datetime.now()
##
##for i in range(5, 0, -1):
##    delta = datetime.timedelta(days = -i) # days 대신 hours seconds 등 다른 시간도 사용 가능
##    date = now + delta
##    print(date)

### 파이썬 300제 244
##import datetime
##
##now = datetime.datetime.now()
##print(now.strftime("%H:%M:%S")) # Y 연도, D 날짜

### 파이썬 300제 245
##import datetime
##
##day = "2020-05-04"
##
##
##ret = datetime.datetime.strptime(day, "%Y-%m-%d")
##print(ret)


# 파이썬 300제 246

##import time
##import datetime
##
##while True:
##    now = datetime.datetime.now()
##    print(now)
##    time.sleep(1)

# 파이썬 300제 247

##import os                   # os.rename() 가장 많이 사용하는 방식이다.
##from os import rename       # rename()
##from os import *            # getcwd(), rename(), ...
##import os as myos           # myos.getcwd()  모듈 이름이 너무 길 때 사용


### 파이썬 300제 248
##import os
##dirt = os.getcwd()
##print(dirt)


### 파이썬 300제 249
##import os
##
##os.rename("C:\\Users\\h\\Desktop\\test.txt", "C:\\Users\\h\\Desktop\\rename.txt")



### 파이썬 300제 250
##
##import numpy
##for i in numpy.arange(0, 5, 0.1):
##    print(i)

### 파이썬 300제 253
##class Human:
##    pass
##
##areun = Human()
##
##print(areun, type(areun))


### 파이썬 300제 254
##class Human:
##    def __init__(self):             # __init__ : 생성자, 어떤 객체가 생성될 때 호출됨
##        print("응애응애")
##
##areum = Human()

### 파이썬 300제 255
##class Human:
##    def __init__(self, name, age, sex):
##        self.name = name
##        self.age = age
##        self.sex = sex
##
##areum = Human("아름", 25, "여자")
##print(areum.name)
##print(areum.age)
##print(areum.sex)

### 파이썬 300제 257
##class Human:
##    def __init__(self, name, age, sex):
##        self.name = name
##        self.age = age
##        self.sex = sex
##
##    def who(self):
##        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))
##
##areum = Human("조아름", 25, "여자")
##areum.who()

### 파이썬 300제 258
##class Human:
##    def __init__(self, name, age, sex):
##        self.name = name
##        self.age = age
##        self.sex = sex
##
##    def who(self):
##        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))
##
##    def setInfo(self, name, age, sex):
##        self.name = name
##        self.age = age
##        self.sex = sex
##
##areum = Human("", 0, "모름")
##areum.who()
##
##areum.setInfo("아름", 25, "여자")
##areum.who()
        
### 파이썬 300제 259

##class Human:
##    def __init__(self, name, age, sex):
##        self.name = name
##        self.age = age
##        self.sex = sex
##
##    def __del__(self):
##        print("나의 죽음을 알리지마라")
##
##    def who(self):
##        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.sex))
##
##    def setInfo(self, name, age, sex):
##        self.name = name
##        self.age = age
##        self.sex = sex
##
##
##areum = Human("아름", 25, "여자")
##del areum
##areum.who()


### 파이썬 300제 261-265
##class Stock:
##    def __init__(self, name, code):
##        self.name = name
##        self.code = code
##
##    def set_name(self, name):
##        self.name = name
##
##    def set_code(self, code):
##        self.code = code
##
##    def get_name(self):
##        return self.name
##
##    def get_code(self):
##        return self.code
##
##삼성 = Stock("삼성전자", "005930")



### 파이썬 300제 266-270
##class Stock:
##    def __init__(self, name, code, per, pbr, 배당수익률):
##        self.name = name
##        self.code = code
##        self.per = per
##        self.pbr = pbr
##        self.배당수익률 = 배당수익률
##
##    def set_per(self, per):
##        self.per = per
##
##    def set_pbr(self, pbr):
##        self.pbr = pbr
##
##    def set_dividend(self, 배당수익률):
##        self.배당수익 = 배당수익률
##        
##stocklist = []
##
##삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
##현대 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
##엘지 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
##
##stocklist.append(삼성)
##stocklist.append(현대)
##stocklist.append(엘지)
##
##print(stocklist[0])
##
##for i in stocklist:
##    print(i.code, i.per)



### 파이썬 300제 271-280
import random

class Account:
    # class variable
    account_count= 0
    
    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withraw_log = []
        
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)   # 숫자를 문자열로 바꾸고 해당 자리수만큼 표현해준다. 빈칸은 0으로 돌려줌
        num2 = str(num2).zfill(2)   # ex. 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    def deposit(self, amount):
        deposit_count = 0
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount
            self.deposit_count += 1

            if self.deposit_count % 5 == 0:
                self.balance *= 1.01

    def deposit_history(self):
        for i in self.deposit_log:
            print(i)

    def withdraw_history(self):
        for i in self.withraw_log:
            print(i)

    def withdraw(self, amount):
        if amount < self.balance:
            self.withraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름 :", self.bank)
        print("예금주 :", self.name)
        print("계좌번호 :", self.account_number)
        print("잔고 : ", self.balance)

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)
         
account_list = []

k = Account("kim", 1100000)
l = Account("lee", 500)
s = Account("song", 20000000)


account_list.append(k)
account_list.append(l)
account_list.append(s)

##print(account_list)

##for i in account_list:
##    if i.balance >= 1000000:
##        i.display_info()

k.deposit(200)
k.deposit(100)

k.deposit_history()
