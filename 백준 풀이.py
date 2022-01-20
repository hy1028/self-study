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
H, M = map(int, input().split())

if H > 0:
    if M > 44:
        print(H, M-45)
    else :
        print(H-1, M+60-45)

else:
    if M > 44:
        print(23, M-45)
    else :
        print(23, M+60-45)
















