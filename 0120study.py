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

per = ["10.31", "", "8.00"]
for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
        







