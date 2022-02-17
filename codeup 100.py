# #6063
# a, b = map(int, input().split(' '))
# c = a if (a >= b) else b
# print(c)

# #6064
# a, b, c = map(int, input().split(' '))
# d = (a if a <= b else b) if (a if a <= b else b) < c else c
# print(d)

# #6065
# a, b, c = map(int, input().split(' '))
# numlist = [a, b, c]
# for i in numlist:
#     if i % 2 == 0:
#         print(i)
#     else:
#         pass

# #6066
# a, b, c = map(int, input().split(' '))
# numlist = [a, b, c]
# for i in numlist:
#     if i % 2 == 0:
#         print('even')
#     else:
#         print('odd')

# #6067
# a = int(input())
# if a < 0:
#     if a % 2 == 0:
#         print('A')
#     else:
#         print('B')
# elif a > 0:
#     if a % 2 == 0:
#         print('C')
#     else:
#         print('D')

# #6068
# t = int(input())
# if t >= 90:
#     print('A')
# elif t >= 70:
#     print('B')
# elif t >= 40:
#     print('C')
# else:
#     print('D')

# #6069
# t = input()
# if t == 'A':
#     print('best!!!')
# elif t == 'B':
#     print('good!!')
# elif t == 'C':
#     print('run!')
# elif t == 'D':
#     print('slowly~')
# else:
#     print('what?')

# #6070
# s = int(input())
# if s >= 12:
#     print('winter')
# elif s >= 9:
#     print('fall')
# elif s >= 6:
#     print('summer')
# elif s >= 3:
#     print('spring')
# else:
#     print('winter')


# #6071
# n = 1
# while n != 0:
#     n = int(input())
#     if n !=0:
#         print(n)
#     else:
#         break

# #6072
# a = int(input())
# while a > 0:
#     print(a)
#     a -= 1

# #6073
# n = int(input())
# a = n - 1
# while a > -1:
#     print(a)
#     a -= 1

# #6074
# a = input()
# b = ord(a)
# s = ord('a')
# while s <= b:
#     print(chr(s), end=' ')
#     s += 1

# #6075
# a = int(input())
# n = 0
# while n <= a:
#     print(n)
#     n += 1

# #6076
# a = int(input())
# for i in range(a+1):
#     print(i)

# #6077
# a = int(input())
# s = 0
# for i in range(a+1):
#     if i % 2 == 0:
#         s += i
#     else:
#         pass
#
# print(s)


# #6078
# n = input()
# print(n)
# while n != 'q':
#     n = input()
#     print(n)
#     if n == 'q':
#         break

# #6079
# a = int(input())
# s = 0
# for i in range(1, a):
#     s += i
#     if s >= a:
#         print(i)
#         break

# #6080
# a, b = map(int, input().split(' '))
# for i in range(1, a+1):
#     for j in range(1, b+1):
#         print(i, j)

# #6081
# n = input()
# n = int(n, 16)
# for i in range(1, 16):
#     print('%X'%n, '*', '%X'%i, '=', '%X'%(n*i), sep='')

# #6082
# n = int(input())
# for i in range(1, n+1):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print('X', end=' ')
#     else:
#         print(i, end=' ')

# #6083
# r, g, b = map(int, input().split(' '))
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             print(i, j, k)
# print(r*g*b)

# #6084
# h, b, c, s = map(int, input().split(' '))
# print(format(h * b * c * s / 8 / 1024/ 1024, '.1f'), 'MB')

# #6085
# w, h, b = map(int, input().split(' '))
# print(format(w * h * b / 8/ 1024/ 1024, '.2f'), 'MB')

# #6086
# n = int(input())
# sum = 0
# for i in range(n+1):
#     sum += i
#     if sum >= n:
#         print(sum)
#         break

# #6087
# n = int(input())
# for i in range(1, n+1):
#     if i % 3 == 0:
#         continue
#     else:
#         print(i, end=' ')

# #6088
# a, b, c = map(int, input().split())
# sum = a
# n = 1
# while n < c:
#     sum += b
#     n += 1
#
# print(sum)

# #6089
# a, b, c = map(int, input().split())
# for i in range(c-1):
#     a *= b
#
# print(a)

# #6090
# a, b, c, d = map(int, input().split())
# for i in range(1, d):
#     a *= b
#     a += c
#
# print(a)

# #6091
# a, b, c = map(int, input().split())
# day = 1
# while day%a !=0 or day%b !=0 or day%c !=0:
#     day += 1
#
# print(day)

# #6092
# n = int(input())
# a = list(map(int, input().split()))
# for i in range(1, 24):
#     count = 0
#     for j in a:
#         if i == j:
#             count += 1
#     print(count, end = ' ')

# #6093
# n = int(input())
# a = list(map(int, input().split()))
# a.reverse()
# for i in a:
#     print(i, end=' ')

#6094
n = int(input())
a = list(map(int, input().split()))
print(min(a))

