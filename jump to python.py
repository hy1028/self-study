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


### 알고리즘 실습 1-7
##
##n = int(input('n값을 입력하세요: '))
##
##total = 0
##i = 1
##
##while i <= n:
##    total += i
##    i += 1
##
##print(total)
    

### 알고리즘 실습 1-8
##
##n = int(input('n값을 입력하세요: '))
##
##total = 0
##for i in range(1, n+1):
##    total += i
##
##print(total)



### 알고리즘 실습 1-13
##
##n = int(input('몇 개를 출력할까요?: '))
##
##for i in range(n // 2):
##    print('+-', end='')
##
##if n % 2 == 1:
##    print('+', end='')



### 알고리즘 실습 1-14
##
##print('*를 출력합니다.')
##n = int(input('몇 개를 출력할까요?: '))
##w = int(input('몇 개마다 줄바꿈할까요?: '))
##
##for i in range(1, n+1):
##    print('*', end="")
##    if i % w == 0:
##        print()
##
##if n % w != 0:
##    print()


### 알고리즘 실습 1-15 (1-14 개선)
##
##print('*를 출력합니다.')
##n = int(input('몇 개를 출력할까요?: '))
##w = int(input('몇 개마다 줄바꿈할까요?: '))
##
##repeat = n // w
##
##for i in range(repeat):
##    print('*' * w)
##
##rest = n % w
##if rest != 0:
##    print('*' * rest)


### 알고리즘 실습 1-16
##
##while True:
##    n = int(input('n값을 입력하세요: '))
##    if n > 0:
##        break
##
##total = 0
##for i in range(1, n+1):
##    total += i
##
##print(f'1부터 {n}까지 정수의 합은 {total}입니다.')
    

### 알고리즘 실습 1-17
##
### 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기
### 내가 짠 알고리즘
##
##area = int(input('직사각형의 넓이를 입력하세요: '))
##
##for i in range(area//2):
##    for n in range(area+1):
##        if i * n == area and i <= n:
##            print(f'{i} x {n}')
##
##
### 책 알고리즘
##
##area = int(input('직사각형의 넓이를 입력하세요: '))
##
##for i in range(1, area + 1):
##    if i * i > area : break     # 첫번째 곱해주는 수의 최대값 한정하기
##    if area % i != 0: continue  # 약수가 아닌경우 조건문의 처음으로 돌아가기
##    else:
##        print(f'{i} x {area // i}')  # i가 약수인 경우 넓이를 두 정수값의 곱으로 표현할 수 있다.




### 알고리즘 실습 1-18
##
### 10~99 사이의 난수 n개 생성하기(13이 나오면 중단)
##
##import random
##
##n = int(input('난수의 개수를 입력하세요.: '))
##
##for i in range(n):
##    r = random.randint(10, 99)
##    print(r, end=' ')
##    if r == 13:
##        print('\n프로그램을 중단합니다.')
##        break
##
##else:
##    print('\n난수 생성을 종료합니다.')    # break문이 실행되지 않았을 경우, 즉 13이 나오지 않았을 경우에만 출력
    

### 알고리즘 실습 1-21
##
##for i in range(1, 10):
##    for j in range(1, 10):
##        print(f'{i * j:3}', end='')
##    print()
    

### 알고리즘 실습 1-22
##
##print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
##n = int(input('짧은 변의 길이를 입력하세요.: '))
##
####for i in range(1, n+1):
####    print('*' * i)
##
##for i in range(n):
##    for j in range(i + 1):
##        print('*', end='')
##    print()
        


### 알고리즘 실습 1-23
##
##print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
##n = int(input('짧은 변의 길이를 입력하세요.: '))
##
####for i in range(1, n+1):
####    공백 = n-i
####    print(' ' * 공백, end=''); print('*' * i)
##
##
##for i in range(1, n+1):
##    for _ in range(n - i):
##        print(' ', end='')
##    for _ in range(i):
##        print('*', end='')
##    print()
    

# 알고리즘 실습 2-3

##from max import max_of
##
### int형 정숫값을 차례로 입력받다가 End를 입력하면 더이상 입력받지 않으며 그 시점에서 원소수를 확정한다.
##
##numlist = []
##a = 0
##while True:
##    n = input(f'list[{a}]값을 입력하세요')
##    if n == "End":
##        break
##    else:
##        num = int(n)
##        a += 1
##        numlist.append(num)
##
##totalnum = len(numlist)
##print(f'{totalnum}개를 입력했습니다.')
##print(f'최댓값은 {max_of(numlist)}입니다.')
    


### 알고리즘 실습 2C-2
##
##x = ['John', 'George', 'Paul', 'Ringo']
##
##for i, name in enumerate(x):
##    print(f'x[{i}] = {name}')



### 알고리즘 실습 2-6
##
##def reverse_array(a):
##    n = len(a)
##    for i in range(n // 2):
##        a[i], a[n-i-1] = a[n-i-1], a[i]
##
##
##if __name__ == '__main__':
##    print('배열 원소를 역순으로 정렬합니다.')
##    num = int(input('원소 수를 입력하세요: '))
##
##    numlist = []
##    for i in range(num):
##        a = int(input(f'numlist[{i}] 값을 입력하세요: '))
##        numlist.append(a)
##
##    reverse_array(numlist)
##    print(numlist)
##    print('배열 원소를 역순으로 정렬했습니다.')
##
##    for b in range(num):
##        print(f'numlist[{b}] = {numlist[b]}')
        


# 알고리즘 실습 2-7
def card_conv(x: int, r: int):
    """정수 x를 r 진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

    d = ''  # 변환 뒤 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]  # 해당하는 문자를 꺼내 결합
        x //= r

    return d[::-1]          # 역순으로 반환


print(card_conv(59, 16))


































