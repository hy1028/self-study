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
        


### 알고리즘 실습 2-7
##def card_conv(x: int, r: int):
##    """정수 x를 r 진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
##
##    d = ''  # 변환 뒤 문자열
##    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##
##    while x > 0:
##        d += dchar[x % r]  # 해당하는 문자를 꺼내 결합
##        x //= r
##
##    return d[::-1]          # 역순으로 반환
##
##
##if __name__ == '__main__':
##    print('10진수를 n진수로 변환합니다.')
##    
##    while True:
##        while True:
##            chg_num = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
##            if chg_num > 0:
##                break
##
##        while True:
##            n = int(input('어떤 진수로 변환할까요?: '))
##            if 2 <= n <= 36:
##                break
##
##        result = card_conv(chg_num, n)
##
##        print(f'{n}진수로는 {result}입니다.')
##
##        choice = input('한 번 더 변환할까요?(Y ... 예 / N ... 아니요): ')
##        if choice == 'N' or choice == 'n':
##            break




### 알고리즘 실습 2-8
##
### 1000 이하의 소수를 나열하기.
##
##counter = 0
##
##for n in range(2, 1001):
##    for i in range(2, n):
##        counter += 1
##        if n % i == 0:
##            break
##
##    else:
##        print(n)
##
##print(counter)


# 알고리즘 실습 2-9

### 내가 작성한 코드 
##prime = [2]
##counter = 0
##
##for n in range(2, 1001):
##    if n > max(prime):
##        for a in prime:
##            counter += 1
##            if n % a == 0:
##                break
##        else:
##            prime.append(n)
##    else:
##        pass
##
##for c in prime:
##    print(c)
##
##print(counter)
        
# 책 참고하여 수정
 
prime = [2]
counter = 0

for n in range(3, 1001, 2):     # 홀수만 지정해준다
    for a in prime[1:]:     # 홀수만 지정 -> prime[0]=2로 나누는 불필요한 계산을 하지 않기 위해 리스트 범위 1: 부터 지정
        counter += 1
        if n % a == 0:
            break
    else:
        prime.append(n)

for c in prime:
    print(c)

print(counter)
























