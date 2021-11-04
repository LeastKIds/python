# num1= 10
# num2 = 20
# print(num1+num2)

# num1 = 1
# num2 = 1.2
# print(num1 + num2)

# print(input())

# print("Hello,", input())

# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)

# num1, num2 = map(int, input().split())
# print(num1 + num2)

# list = [1,2,3,4,5]
# print(list.sort(reverse=True))
# print(list)

# list = [1,2,3,4,5]
# list.insert(0,6)
# list.append(0)
# print(list)
# list.sort()
# print(list)

# list = [1,2,3,4,5]
# list.remove(int(input()))
# print(list)

# multi1= """ hello
# fasadsfa """
# print(multi1)
# str = 'hello my friend'
# str = str.split(' ')
# str_list = list(str)
# print(str_list)

# list = [1,2,3,4,5]
# list[1:4] = [100,200]
# print(list)

# str = input()
# # str = list(str)
# print(str[:3]+str[-3:])
# set1 = set([1,2,3,4])
# set2 = {(1,2),2,3,'Hello'}
# # print(set1)
# # print(set2)
# # set1.add(5)
# # print(set1)
# # set1.add(1)
# # set1.update([7,8])
# # print(set1 - set2)
# print(set1[1])


# num = int(input())
# if num >= 0 :
#     print("OK")
# else:
#     print("NG")

# str = input()
# if len(str) >= 8:
#     print('OK')
# else:
#     print('NG')

# num1, num2 = map(int, input().split())
# if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
#     print('OK')
# else:
#     print('NG')

# num = int(input())
# if num%2 == 0:
#     print('even')
# else:
#     print('odd')

# str = input()
# if 4 <= len(str) <= 10:
#     print('ok')
# else:
#     print('ng')

# num1, num2 = map(int, input().split())
# print('ok' if num1 + num2 >=0 else 'ng')

# num1, num2 = map(int, input().split())
# str = input()
# print(num1 + num2 if str == '+' else num1 - num2)

# list = [1,2,3,4,5,6,7,8,9]
# for i in list[1::2]:
#     print(i)

# list = [1,2,3,4,5,6,7,8,9]
# odd = 0
# even = 0
# for i in list:
#     if i%2==0:
#         even += i
#     else:
#         odd +=i
#
# print(even)
# print(odd)

# for i in range(2, 10):
#     print(2,'X',i,'=',2*i)

# for i in range(4):
#     for j in range(i+1):
#         print('*', end='')
#     print()

# list = [i for i in range(1,11) if i%2 !=0]
# print(list)

# list = [i * 3 for i in range(1,11)]
# print(list)

# n = int(input())
# arr1 = [int(input()) for i in range(n)]
# arr2 = [i for i in arr1 if i >= 0]
# print(arr1)
# print(arr2)

# arr_id = ['12101', '12102', '12103', '12104']
# arr_score = [80,90,90,70,80]
# dic = {key:value for key,value in zip(arr_id, arr_score)}
# print(dic)

# result = 0
# while True:
#     value = int(input())
#     if value == 0:
#         break
#     result +=value
#
# print(result)

# def bigger():
#     num1, num2 = map(int, input().split())
#     if num1 > num2:
#         print(num1)
#     else:
#         print(num2)
#
# bigger()

# def sum_int(*d):
#     value = 0
#     for i in d:
#         if type(i) is int:
#             value +=i
#
#     print(value)
#
# sum_int(1,1,1.0,'1',True)

# def func(first, second):
#     print(first, second)
#
# dic = {'first' : 123, 'second' : 345}
# func(**dic)

# def min_int(list):
#     min = list[0]
#     for i in list:
#         if min > i:
#             min = i
#
#     return min
#
# list2 = [3,4,5,1,2]
# print(min_int(list2))

# list = [1,2,3,4,5]
#
# def info(list2):
#     sum = 0
#     for i in list2:
#         sum += i
#     return sum, sum/len(list2)
#
# sum, avg = info(list)
# print(sum, avg)

# list = [1,2,3,4,5]
#
# def min_max(list2):
#     min = list2[0]
#     max = list2[0]
#     for i in list:
#         if min > i:
#             min = i
#         if max < i:
#             max = i
#     return max, min
#
# max1, min1 = min_max(list)
# print(max1, min1)

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact
#
# def re_factorial(n):
#     if n == 1:
#         return n
#     return n * re_factorial(n-1)
# print(factorial(5))
# print(re_factorial(5))


# def my_generator():
#     print('1#')
#     yield 1
#     print('2#')
#     yield 2
#     print('3#')
#     yield 3
# #
# # list = [i for i in my_generator()]
# # print(list)
#
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def my_range(*num):
#     start = 0
#     end = 0
#     step = 1
#     if len(num) == 1:
#         start = 0
#         end = num[0]
#     else:
#         start = num[0]
#         end = num[1]
#         if len(num) == 3:
#             step = num[2]
#
#     while start < end:
#         yield start
#         start += step
#
# print([i for i in my_range(5)])
# print([i for i in my_range(2,5)])
# print([i for i in my_range(1,10,2)])

# def add(first, second):
#     return first + second
#
# def sub(first, second):
#     return first - second
#
# def executor(func, op, param1, param2):
#     return func[op](param1, param2)
#
# func = {'+': add, '-': sub}
# print(executor(func, '+', 1,2))
# print(executor(func, '-', 1,2))

# def calculate(op):
#     def add(num1, num2):
#         return num1 + num2
#     def sub(num1, num2):
#         return num1 - num2
#
#     if op == '+':
#         return add
#     else:
#         return sub
#
# print(calculate('+')(1,2))
# print(calculate('-')(1,2))

# def func():
#     value = 2
#     def nested_func():
#         nonlocal value
#         value = 3
#         print('nested', value)
#     nested_func()
#     print('outer', value)
#
# func()

# list = [None] * 10
# top = None
#
# def push(num):
#     global top
#     for i in range(len(list)):
#         if list[i] == None:
#             list[i] = num
#             top = num
#             return
#     print('stack overflow')
#     return
#
# def pop():
#     global top
#     if list[0] == None:
#         print('stack empty')
#         return
#     print(top)
#     n = list.index(top)
#     list[n] = None
#     top = list[n -1]
#     return
#
# for i in range(11):
#     push(i)
#     print(list)
#
# for i in range(11):
#     pop()

# list = []
# front=None
# def put(num):
#     global front
#     if len(list)==0:
#         front = num
#     list.append(num)
#
# def get():
#     global front
#     if len(list) == 0:
#         print('error')
#         return
#     print(front)
#     del list[0]
#     if len(list) == 0:
#         return
#     front = list[0]
#
# put(1)
# print(list)
# get()
# get()
# num = int(input())
# list = [1,3,6,9,12,15,18,21]
# while True:
#     list_len = len(list)
#     if list_len == 2:
#         if list[0] == num or list[1] == num:
#             print('yes')
#             break
#         else:
#             print('no')
#             break
#     if num == list[list_len//2]:
#         print('yes')
#         break
#     elif num >= list[list_len//2]:
#         list = list[list_len//2:]
#         continue
#     else:
#         list = list[:list_len//2]
#         continue


# def merge_sort(list):
#     if len(list)<=1:
#         return list
#
#     mid = len(list)//2
#     # print(merge_sort(list[:mid]))
#     print(merge_sort(list[mid-1:]))
#     # print(mid)
#
#
# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
#
#     mid = len(arr) // 2
#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])
# list = [6, 5, 3]
# merge_sort(list)

# def merge_sort(listL):
#     if len(listL) == 1:
#         return listL
#
#     mid = len(listL) // 2
#     leftMerge = merge_sort(listL[:mid])
#     rightMerge = merge_sort(listL[mid:])
#     return merge(leftMerge, rightMerge)
#
#
# def merge(leftMerge, rightMerge):
#     result = []
#     while len(leftMerge) > 0 or len(rightMerge) > 0:
#
#         if len(leftMerge) > 0 and len(rightMerge) > 0:
#             if leftMerge[0] > rightMerge[0]:
#                 result.append(rightMerge[0])
#                 rightMerge = rightMerge[1:]
#             elif leftMerge[0] < rightMerge[0]:
#                 result.append(leftMerge[0])
#                 leftMerge = leftMerge[1:]
#         elif len(leftMerge) > 0:
#             result.append(leftMerge[0])
#             leftMerge = leftMerge[1:]
#         elif len(rightMerge) > 0:
#             result.append(rightMerge[0])
#             rightMerge = rightMerge[1:]
#
#     return result
#
#
#
#
# list = [4,2,1,6,9,19,29,15]
# # list = [4,2,1]
# print(merge_sort(list))

# def print_itmes(param):
#     print(param)
#     for p in param:
#         print(p)
#
# print_itmes((i for i in range(3)))

# def my_range(*list):
#     start = 0
#     step = 1
#     end = 0
#     if len(list) == 1:
#         end = list[0]
#     else:
#         start = list[0]
#         end = list[1]
#         if len(list) == 3:
#             step = list[2]
#
#     while start < end:
#         print(start, end='')
#         start += step
#     print()
#
# my_range(5)
# my_range(2,5)
# my_range(1,10,2)

# str = 'hello my friend'
# split_default = str.split()
# split_char = str.split('e')
#
# str_list = list(str)
# print('*'.join(split_default))
# print('-'.join(split_char))

# set1 = set([1,2,3,4])
# print(set1)

# def merge_sort(listL):
#     if len(listL) <= 1:
#         return listL
#     mid = len(listL) // 2
#     leftMerge = merge_sort(listL[:mid])
#     rightMerge = merge_sort(listL[mid:])
#     return merge(leftMerge, rightMerge)
#
# def merge(leftMerge, rightMerge):
#     result = []
#     while len(leftMerge) > 0 or len(rightMerge):
#         if len(leftMerge) > 0 and len(rightMerge):
#             if leftMerge[0] > rightMerge[0]:
#                 result.append(rightMerge[0])
#                 rightMerge = rightMerge[1:]
#             else:
#                 result.append(leftMerge[0])
#                 leftMerge = leftMerge[1:]
#         elif len(leftMerge) > 0 and len(rightMerge) <= 0:
#             result.append(leftMerge[0])
#             leftMerge = leftMerge[1:]
#         elif len(rightMerge) > 0 and len (leftMerge) <= 0:
#             result.append(rightMerge[0])
#             rightMerge = rightMerge[1:]
#
#     return result
#
# list = [4,1,6,7,13,16,11,20,19]
# # print(merge_sort(list))
#
# def merge_sort(listL, low, high):
#     if low >= high:
#         return
#     mid = (low + high) // 2
#     merge_sort(listL, low, mid)
#     merge_sort(listL, mid+1, high)
#     merge(listL, low, mid, high)
#
# def merge(listL, low, mid ,high):
#     l = low
#     h = high
#     r = mid+1
#     result = []
#     while l <= mid and h >= r:
#         print(result)
#         if listL[l] < listL[r]:
#             result.append(listL[l])
#             l += 1
#         else:
#             result.append(listL[r])
#             r += 1
#
#     print('end')
#     if l > mid:
#         result.extend(listL[r:h+1])
#     elif r > h:
#         result.extend(listL[l:mid+1])
#
#     list[low:high+1] = result
#     return list
#
# print(merge_sort(list, 0, 8))

def merge_sort(list, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(list, low, mid)
    merge_sort(list, mid+1, high)
    merge(list, low, mid, high)

def merge(list, low, mid, high):
    l = low
    r = mid + 1
    temp = []
    while l <= mid and r <= high:
        if list[l] < list[r]:
            temp.append(list[l])
            l += 1
        else:
            temp.append(list[r])
            r += 1
    if l > mid:
        temp.extend(list[r:high+1])
    elif r > high:
        temp.extend(list[l:mid+1])
    list[low:high+1] = temp
    print(list)

list = [8,7,6,5,4,3,2,1]
merge_sort(list, 0, 7)

# def sum_int(*params):
#     sum = 0
#     for p in params:
#         if type(p) == bool:
#             print(p)
#
#
# sum_int(1,1,1.0,'1',True)