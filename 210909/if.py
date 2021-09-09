# value = int(input())
#
# if value > 0:
#     print('OK1')
# elif value == 0:
#     print('OK2')
# elif value < 0:
#     print('NG')


# value = input()
#
# if len(value) >= 8:
#     print('OK')
# else:
#     print('NG')

# a, b = map(int, input().split())
#
# if (a < 0 and b < 0) or (a > 0 and b > 0):
#     print('OK')
# else:
#     print('NG')

# a = int(input())
#
# if a%2 != 0:
#     print('odd')
# else:
#     print('even')

# value = input()
#
# if 4 <= len(value) <= 10:
#     print('OK')
# else:
#     print('NG')

# a, b = map(int, input().split())
#
# print('OK') if a + b >= 0 else print('NG')

# n1, n2 = map(int, input().split())
# value = input()
#
# print(n1 + n2) if value == '+' else print(n1 - n2)

# arr = [1,3,5,7]
# # for a in arr:
# #     print(a)
#
# # for b in [2,4,6,8]:
# #     print(b)
#
# for c in arr[2:]:
#     print(c)

# tp = (1,2,3,4,5)
#
# for t in tp:
#     print(t)
#
# str = 'Hello everyone'
# for s in str:
#     print(s)

# tp = [1,2,3,4,5,6,7,8,9]
#
# for t in tp:
#     if t % 2 == 0:
#         print(t)

# arr = [1,2,3,4,5,6,7,8,9]
# a=0
# b=0
# # for ar in arr:
# #     if ar % 2 == 0:
# #         a += ar
# #     else:
# #         b += ar
#
# last = len(arr)
# for i in arr[1:last:2]:
#     a += i
# for i in arr[0:last:2]:
#     b += i
#
# print(a, b)

# for i in range(5):
#     print(i)
# for i in range(5,10):
#     print(i)
# for i in range(1,10,2):
#     print(i)

# for i in range(2,10):
#     print('2 X ', i ,' = ' ,2*i)

# for i in range(1, 5):
#     for k in range(0, i):
#         print('*', end='')
#     print()

# arr = [10, 11, 12, 13]
# for index, value in enumerate(arr):
#     print(index, value)
# arr = ['J', 'K', 'S']
# for i, v in enumerate(arr):
#     print(i, v)

# arr1 = [10, 11, 12, 13]
# arr2 = [1, 2, 3, 4]
# arr3 = ['hello', 'my', 'friend']
#
# for i, j, k in zip(arr1, arr2, arr3):
#     print(i, j, k)

# arr = [i for i in range(5, 10)]
# print(arr)
#
# arr = [2*i for i in range(3)]
# print(arr)
#
# arr = [[i, j] for i in range(3) for j in range(10, 13)]
# print(arr)

# arr = [i for i in range(1, 10, 2)]
# print(arr)

# arr = [i*3 for i in range(1, 11)]
# print(arr)

# arr = [i for i in range(10) if i%2 == 0]
# print(arr)
#
# scores = [80, 95, 66, 88, 90, 70, 74, 98]
# a_grade = [s for s in scores if s >= 90]
# print(a_grade)

# n = int(input())
# arr1 = [int(input()) for _ in range(n)]
# arr2 = [i for i in arr1 if i >= 0]
# for a in arr2:
#     print(a)

# set1 = {i for i in range(5)}
# print(set1)
# arr = [1, 1, 1, 2, 2, 3, 3, 3]
# set2 = {i for i in arr}
# print(set2)

# arr_id = ['12101', '12102', '12103', '12104']
# arr_score = [80, 80, 90, 70, 80]
# dic = {key:value for key,value in zip(arr_id, arr_score)}
# print(dic)

# arr_id = ['12101', '12102', '12103', '12104']
# arr_score = [80, 90, 90, 70, 80]
# dic = {key:value for key,value in zip(arr_id, arr_score) if value > 80}
# print(dic)

# arr = [i for i in range(10)]
#
# while True:
#     print('Enter number : ', end = ' ')
#     value = int(input())
#     if value not in arr:
#         print('exit')
#         break

result = 0
while True:
    value = int(input())
    if value == 0:
        break
    result += value
print(result)