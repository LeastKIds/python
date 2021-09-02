# str = input()
# age = int(input())
# score = float(input())
# print(str, age, score)
#
# first_name, last_name = input().split()
# print(first_name, last_name)
#
# year, month = map(int, input().split())
# print(year, month)

# str = input().split()
#
# print(str)

# x = 10
# y = 20
#
# print(x + y)
#
# x = 10
# y = 4.5
#
# print(x+y)
#
# x = input()
# print('Hello,', x)
#
# x = int(input())
# y = int(input())
# print(x + y)
#
# x, y = map(int, input().split())
# print(x + y)

# print('\    /\ ')
# print(' )  ( \') ')
# print('(  /  )')
# print(' \(__)|')

# x, y = map(int, input().split())
# print(x + y)
# print(x - y)
# print(x * y)
# print(int(x / y))
# print(x % y)

a, b, c = map(int, input().split())
print(int((a + b) % c))
print(int(((a % c) + (b % c)) % c))
print(int((a*b)%c))
print(int(((a%c) * (b%c))%c))
