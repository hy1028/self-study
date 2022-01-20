# 파이썬 300제 281-287

##class 차:
##    def __init__(self, 바퀴, 가격):
##        self.바퀴 = 바퀴
##        self.가격 = 가격
##
##    def 정보(self):
##        print("바퀴수", self.바퀴)
##        print("가격", self.가격)
##
##class 자전차(차):
##    def __init__(self, 바퀴, 가격, 구동계):
##        super().__init__(바퀴, 가격)            #super()는 부모클래스를 의미
##        #차.__init__(self, 바퀴, 가격)          #위와 동일한 의미. 보통 super() 사용을 권장 
##        self.구동계 = 구동계
##
##    def 정보(self):
##        super().정보()
##        print("구동계", self.구동계)
##
##
##class 자동차(차):
##    def __init__(self, 바퀴, 가격):
##        super().__init__(바퀴, 가격)
##        
##
##bicycle = 자전차(2, 100, "시마노")
##bicycle.정보()


# 파이썬 300제 291
##f = open("C:\\Users\\h\\Desktop\\매수종목1.txt", mode="wt", encoding="utf-8")       #내용에 한글이 있는 경우 utf-8 써주는게 좋음.
##f.write("005930\n")
##f.write("005380\n")
##f.write("035420")
##f.close()


# 파이썬 300제 292
##f = open("C:\\Users\\h\\Desktop\\매수종목2.txt", mode="wt", encoding="utf-8")       #내용에 한글이 있는 경우 utf-8 써주는게 좋음.
##f.write("005930 삼성전자\n")
##f.write("005380 현대차\n")
##f.write("035420 NAVER")
##f.close()


# 파이썬 300제 293
##import csv
##f = open("C:\\Users\\h\\Desktop\\매수종목.csv", mode="wt", encoding="cp949", newline='')        #newline이 지정된 경우 자동 엔터됨, 생략해주었음.
##writer = csv.writer(f)
##writer.writerow(["종목명", "종목코드", "PER"])
##writer.writerow(["삼성전자", "005930", 15.79])
##writer.writerow(["NAVER", "035420", 55.82])
##f.close()


# 파이썬 300제 294
##f = open("C:\\Users\\h\\Desktop\\매수종목1.txt", mode="r", encoding="utf-8") # 읽기의 경우 mode 생략 가능
##lines = f.readlines()   #python list
##
##codelist = []
##for line in lines:
##    code = line.strip() #'\n' 제거
##    codelist.append(code)
##
##print(codelist)
##
##f.close()


#파이썬 300제 295
##f = open("C:\\Users\\h\\Desktop\\매수종목2.txt", mode="r", encoding="utf-8")
##lines = f.readlines()

### 내가 작성한 코드
##list1 = []
##for line in lines:
##    code = line.strip()
##    list1.append(code)
##
##codedic = {}
##for code in list1:
##    codedic[code[:6]]=code[7:]
##    
##print(codedic)


###정답 코드
##codedic = {}
##for line in lines:
##    line = line.strip()
##    k, v = line.split(" ")
##    codedic[k] = v
##
##print(codedic)
##
##f.close()


# 파이썬 300제 296-297

##per = ["10.31", "", "8.00"]
##perlist = []
##
##for i in per:
##    try:
##        new = float(i)
##    except:
##        new = 0
##    perlist.append(new)
##
##print(perlist)


# 파이썬 300제 298

##try:
##    b = 3 / 0
##except ZeroDivisionError:
##    print("0으로 나눌 수 없습니다.")


# 파이썬 300제 299
##data = [1, 2, 3]
##
##for i in range(5):
##    try:
##        print(data[i])
##    except IndexError as e:
##        print(e)

# 파이썬 300제 300

##per = ["10.31", "", "8.00"]
##for i in per:
##    try:
##        print(float(i))
##    except:
##        print(0)
##    else:
##        print("clean data")
##    finally:
##        print("변환 완료")
        

### 알고리즘 실습 1-1
##
### 세 정수를 입력받아 최댓값 구하기
##
##print('세 정수의 최댓값을 구합니다.')
##a = int(input('정수 a의 값을 입력하세요.: '))
##b = int(input('정수 b의 값을 입력하세요.: '))
##c = int(input('정수 c의 값을 입력하세요.: '))
##
##maximum = a
##if b > maximum:
##    maximum = b
##if c > maximum:
##    maximum = c
##
##print(f'최댓값은 {maximum}입니다.')


### 알고리즘 실습 1C-1
##
##name = input('이름을 입력하세요.: ')
##print(f"안녕하세요? {name} 님.")
##


### 알고리즘 실습 1-2
##
###최대값 구하기 함수버전
##
##def max3(a, b, c):
##    maximum = a
##    if b > maximum:
##        b = maximum
##    if c > maximum:
##        c = maximum
##    return maximum
##
##print(max(9,2,6))

### 알고리즘 실습 1C-2
### 세 정수 중 중앙값 구하기

##def med3(a, b, c):
##    intlist = [a, b, c]
##    intlist.sort()
##    return intlist[1]
##
##print(med3(5, 7, 9))

##def med3(a, b, c):
##    if a >= b:
##        if b >= c:
##            return b
##        elif c >= a:
##            return a
##        else: return c
##    elif a > c:
##        return a
##    elif b > c:
##        return c
##    else :
##        return b
##
##print(med3(5, 7, 1))


# 알고리즘 실습 1-7

n = int(input('n값을 입력하세요: '))

total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(total)
    





