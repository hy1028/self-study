# 1000번
##A, B = map(int, input().split()) # map(적용할함수, 반복가능한자료형) 사용 시 자료형 각각에 함수를 적용해준다.
##print(A + B)


# 1001번
##A, B = map(int, input().split())
##print(A - B)


# 10869번
##A, B = map(int, input().split())
##print(A + B)
##print(A - B)
##print(A * B)
##print(A // B)
##print(A % B)

#10430번
##A, B, C = map(int, input().split())
##print((A+B)%C)
##print(((A%C) + (B%C))%C)
##print((A*B)%C)
##print(((A%C) * (B%C))%C)


# 2588번
##a = int(input())
##b = input()
##
##print(a * int(b[2]))
##print(a * int(b[1]))
##print(a * int(b[0]))
##print(a * int(b))


#1330번
##A, B = map(int, input().split())
##if A > B:
##    print('>')
##elif A < B:
##    print('<')
##else:
##    print('==')


# 9498번
##a = int(input())
##if 90 <= a <= 100:
##    print('A')
##elif 80 <= a <= 89:
##    print('B')
##elif 70 <= a <= 79:
##    print('C')
##elif 60 <= a <= 69:
##    print('D')
##else:
##    print('F')


#2753번
##year = int(input())
##if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
##    print(1)
##else:
##    print(0)

# 14681번
##x = int(input())
##y = int(input())
##if x > 0 and y > 0:
##    print(1)
##elif x < 0 and y > 0:
##    print(2)
##elif x < 0 and y < 0:
##    print(3)
##else:
##    print(4)


# 2884번
##H, M = map(int, input().split())
##
##if M >= 45:
##    print(H, M-45)
##elif M < 45 and H > 0:
##    print(H - 1, M + 15)
##else:
##    print(23, M + 15)



# 2739번

##N = int(input())
##
##for i in range(1, 10):
##    print(f'{N} * {i} = {N * i}')
    

# 10950번
##T = int(input())
##
##for i in range(T):
##    A, B = map(int, input().split())
##    print(A + B)

#8393번
##n = int(input())
##
##total = 0
##for i in range(1, n+1):
##    total += i
##
##print(total)



#15552번
##import sys
##
##T = int(input())
##
##for i in range(T):
##    A, B = map(int, sys.stdin.readline().split())   #input() 대신 sys.stdin.readline()을 사용하면 시간단축됨
##    print(A + B)                                    #반복문에 input 사용 시 시간초과 될 수 있음.


#2741번
##N = int(input())
##
##for i in range(1, N+1):
##    print(i)


# 2742번
##N = int(input())
##
##for i in range(N):
##    print(N - i)


#11021번
##t = int(input())
##
##for i in range(1, t+1):
##    a, b = map(int, input().split())
##    print(f'Case #{i}: {a + b}')


#11022번
##t = int(input())
##
##for i in range(1, t+1):
##    a, b = map(int, input().split())
##    print(f'Case #{i}: {a} + {b} = {a + b}')


###2438번
##n = int(input())
##
##for i in range(1, n+1):
##    print('*' * i)


#2439번
##n = int(input())
##
##for i in range(1, n+1):
##    print(' ' * (n-i), end=''); print('*' * i)

    
#10871
##n, x = map(int, input().split())
##a = input().split()
##
##for i in a:
##    b = int(i)
##    if b < x:
##        print(b, end=' ')


#10952번
##while True:
##    a, b = map(int, input().split())
##    if a == 0 and b == 0:
##        break
##    else:
##        print(a + b)

#10951번
##while True:
##    try:
##        a, b = map(int, input().split())
##    except:
##        break
##    else:
##        print(a + b)

#1110번
##n = int(input())
##firstn = n
##count = 0
##while True:
##    a = n//10 + n%10
##    add = a%10
##    n = ((n%10)*10) + add
##    count += 1
##    if n == firstn:
##        break
##print(count)


#10818번
##import sys
##n = int(input())
##nlist = map(int, sys.stdin.readline().split())
##nlist = list(nlist)             # map class는 인덱싱이 불가하여 list형으로 캐스팅함.
##
##print(min(nlist),end = ' '); print(max(nlist))


#2562번

##nlist = [int(input()) for i in range(9)]    # 리스트내포로 표현해보았음
##print(max(nlist))
##print(nlist.index(max(nlist)) + 1)


#2577번
##a = int(input())
##b = int(input())
##c = int(input())
##
##total = a * b * c
##
##for i in range(10):
##    print(str(total).count(str(i)))

#3052번
##nlist = []
##for i in range(10):
##    nlist.append(int(input()) % 42)
##
##print(len(set(nlist)))


#1546번
##n = int(input())
##sl = list(map(int, input().split(' ')))
##
##max_s = max(sl)
##
##for i in range(n):
##    sl[i] = sl[i] / max_s * 100
##
##print(sum(sl)/n)
       

#8958번
##n = int(input())
##i = 0
##
##while i < n:
##    c = input()
##    score = 0
##    sl = []
##    for a in range(len(c)):
##        if c[a] == 'O':
##            score += 1
##            sl.append(score)
##        else:
##            score = 0
##    print(sum(sl))
##    i += 1          #while문 종료를 위해 넣어줌    


#4344번
##c = int(input())
##a = 0
##
##while a < c:
##    testcase = list(map(int, input().split()))
##    num = testcase[0]
##    average = sum(testcase[1:])/num
##
##    count = 0
##    for i in range(1, num+1):
##        if testcase[i] > average:
##            count += 1
##
##    result = round(count/num*100, 3)
##
##    print(f'{result:.3f}%')
##    a += 1

#15596번
##def solve(a):
##    ans = sum(a)
##
##    return ans        

#4673번
##def d(n):
##    a = sum(map(int, str(n)))
##    return n + a
##
##nsn = []    # non-self number list 생성
##for i in range(1, 10001):
##    nsn.append(d(i))
##
##for j in range(1, 10001):
##    if j in nsn:
##        pass
##    else:
##        print(j)
    

#1065번
##def sol(n):
##    if n < 100:
##        return n
##    else :
##        dl = list(map(int, str(n)))
##        ml = []
##        for i in range(len(dl)-1):
##            ml.append(dl[i] - dl[i+1])
##
##        nml = list(set(ml))
##        if len(nml) == 1:
##            return n
##
##a = int(input())
##nlist = []
##
##for i in range(1, a+1):
##    if sol(i) != None:
##        nlist.append(sol(i))
##
##print(len(nlist))

##n = int(input())
##if n < 100 :
##    hs = n
##else:
##    hs = 99
##    for i in range(100, n+1):
##        dl = list(map(int, str(i)))
##        if dl[0] - dl[1] == dl[1] - dl[2]:
##            hs += 1
##
##print(hs)


#10926번

##a = input()
##print(f'{a}??!')



#18108번
##a = int(input())
##print(a - 543)



#11654번
#ord 함수 사용 시 바로 풀이 가능함

##list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
##list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
##list3 = []
##
##for i in list2:
##    list3.append(i.upper())
##
##a = input()
##
##if a in list1:
##    for i in list1:
##        if i != a:
##            pass
##        else:
##            print(48 + list1.index(i))
##
##if a in list2:
##    for j in list2:
##        if j != a:
##            pass
##        else:
##            print(97 + list2.index(j))
##
##if a in list3:
##    for k in list3:
##        if k != a:
##            pass
##        else:
##            print(65 + list3.index(k))

##print(ord(input()))


#11720번
##num1 = input()
##num2 = input()
##
##numlist = map(int, list(num2))
##print(sum(numlist))

# 다른 풀이
##num1 = input()
##num2 = input()
##
##total = 0
##for i in num2:
##    total += int(i)
##
##print(total)


# 10809번
##import string   # 알파벳 리스트 불러올 수 있는 모듈 
##
##a = input()
##b = list(string.ascii_lowercase)
##
##for i in b:
##    if i in a:
##        print(a.index(i))
##    else:
##        print(-1)


#2675번
##num = int(input())
##for i in range(num):
##    a, b = input().split()
##    for j in b:
##        print(j * int(a), end='')
##    print()


#1157번
##a = input()
##b = list(a.upper())
##bset = set(b)
##setlist = list(bset)
##
##count = []
##for i in setlist:
##    count.append(b.count(i))
##
##dic = dict(zip(count, setlist))
##
##count.sort()
##count.reverse()
##
##if len(setlist) == 1:
##    print(setlist[0])
##elif len(count) == 1:
##    print('?')
##elif count[0] == count[1]:
##    print('?')
##else:
##    print(dic[max(count)])

# 다른풀이
##import string
##
##word = input().upper()
##abc = list(string.ascii_uppercase)
##
##r = 0
##count = 0
##for a in abc:
##    temp = word.count(a)
##    if temp != 0:
##        if r < temp:
##            r = temp
##            count = a
##        elif r == temp:
##            count = '?'      
##print(count)








