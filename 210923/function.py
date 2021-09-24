# def say_hello():
#     print('hello')
#
# def say_bye():
#     print('bye')
#
# say_hello()
# say_bye()

# def say_hello(name):
#     print('hello', name)
#
# def say_bye(name):
#     print('bye', name)
#
# say_hello('everyone')
# say_bye('everyone')
#
# def add(first, second):
#     print(first,'+',second,'=',first + second)
#
# # add(1, 2)
# # add(10, 20)
#
# add(second='1', first = '2')

# a, b = map(int, input().split())
#
# def bigger(a,b):
#     # if a>b:
#     #     print(a)
#     # else:
#     #     print(b)
#     print(a if a>b else b)
#
# bigger(a,b)

# def hello(age, name='user'):
#     print('hello', name, age)
#
# hello(20)
# hello(20,'abc')

# def print_tp(*t):
#     print(t)
#
# def print_dic(**d):
#     print(d)
#
# print_tp(1,2,3,4,5)
# print_dic(first=1, second=2, third=3)


# def sum(*t):
#     result = 0
#     for value in t:
#         if type(value) is int:
#             print(value,'int')
#             result += value
#
#     print(result)
#
# sum(1,1,1.0,'1',True)

# def param1(a,b,c=5, *t):
#     print(c)
#     print(t)
# def param2(a,*t, b,c=3):
#     print(c)
#     print(t)
# def param3(*t, a,b,c=3):
#     print(c)
#     print(t)
#
# param1(1,2,3,4)
# param2(1,2,3,b=4)
# param3(1,2,a=3,b=5,c=6)

# def func(first, second):
#     print(first, second)
#
# param1=[1,2]
# param2=(3,4)
# func(*param1)
# func(*param2)
# func(*[5,6])
#
# dic = {'first' : 1, 'second' : 2}
# func(**dic)

# def add(first, second):
#     return first + second
#
# print(add(1,2))
# result = add(1,2)
# print(result)

# def min_int(list):
#     min = list[0]
#     for m in list:
#         if m < min:
#             min = m
#
#     return min
#
# list = [1,2,-3,4,5]
# print(min_int(list))

# def func():
#     return 1,2,3
#
# tp = func()
# print(type(tp))
# x, y, z = func()
# x=10

# def info(list):
#     sum=0
#     for l in list:
#         sum += l
#
#     avg = sum/len(list)
#     return sum, avg
#
# list = [x for x in range(1,10)]
#
# sum, avg = info(list)
# print('sume=',sum,'avg=',avg)

# def min_max(list):
#     min=list[0]
#     max=list[0]
#     for l in list:
#         if min > l:
#             min = l
#         if max < l:
#             max = l
#     return max, min
#
# list = [x for x in range(1,10)]
# max, min = min_max(list)
# print('max',max,'min',min)

# sum = 0
# def total(values):
#     global sum
#     sum = 0
#     for i in values:
#         sum +=i
#     print(sum)
#
# total([1,2,3])
# print(sum)

# def func(first, second):
#     first +=10
#     second.add(4)
#
# number = 1
# set = {1,2,3}
# func(number, set)
# print(number ,set)

# def func():
#     return 1, 1.0
#
# print(type(func()))

# def count_down(n):
#     if n == 0:
#         return
#     print(n)
#     count_down(n-1)
#
# count_down(5)

# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result *=i
#
#     return result
#
# print(factorial(1))
# print(factorial(3))
# print(factorial(5))
#
# def re_factorial(n):
#     if n==1:
#         return 1
#     else:
#         result = n * re_factorial(n-1)
#         return result
#
# print(re_factorial(1))
# print(re_factorial(3))
# print(re_factorial(5))

# def print_items(param):
#     for p in param:
#         print(p)
#
# print_items((i for i in range(3)))

# def my_generator():
#     print('return 1')
#     yield 1
#     print('return 2')
#     yield 2
#     print('return 3')
#     yield 3
#
# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def my_range(*list):
#     step = 1
#     start=0
#     end=0
#     if len(list) == 1:
#         end=list[0]
#     else:
#         start=list[0]
#         end=list[1]
#         if len(list) == 3:
#             step = list[2]
#
#     while start < end:
#         yield start
#         start += step
#
# list1 = [i for i in my_range(5)]
# print(list1)
# list2 = [i for i in my_range(2,5)]
# print(list2)
# list3 = [i for i in my_range(1,10,2)]
# print(list3)

# def add(first, second):
#     return first + second
# def sub(first, second):
#     return first - second
# def executor(func, op, param1, param2):
#     return func[op](param1,param2)
#
# func = {'+' : add, '-' : sub}
# print(executor(func,'+',1,2))
# print(executor(func,'-',1,2))

# def add(first, second):
#     return first + second
# def sub(first, second):
#     return first - second
# def get_func(op):
#     if op == '+':
#         return add
#     else:
#         return sub
#
# result = get_func('+')(1,2)
# print(result)

# def calculate(op, num1, num2):
#     def add(num1, num2):
#         return num1 + num2
#     def sub(num1, num2):
#         return num1 - num2
#
#     if op == '+':
#         return add(num1,num2)
#     else:
#         return sub(num1,num2)
#
# print(calculate('+',1,2))

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

# def func():
#     value = 2
#     def nested_func():
#         value=3
#         print('nested', value)
#     nested_func()
#     print('outer',value)
#
# func()

# def func():
#     value = 2
#     def nested_func():
#         nonlocal value
#         value=3
#         print('nested', value)
#     nested_func()
#     print('outer',value)
#
# func()

# def func():
#     value = 2
#     def nested_func():
#         print('nested', value)
#     nested_func()
#     print('outer',value)
#
# func()

# selection = int(input())
# if selection == 1:
#     def func():
#         print('hello')
# else:
#     def func():
#         print('bye')
#
# func()

# def scale_up():
#     scale = 10
#     def calculate(number):
#         return number * scale
#     return calculate
#
# func = scale_up()
# print(func(10))

# list = [1,2,3]
# value=0
# try:
#     index = int(input())
#     value = list[index]
# except (ValueError, IndexError):
#     value = list[0]
# finally:
#     print(value)

# num = int(input())
# try:
#     value = 10/num
# except Exception as err:
#     print(err)
# else:
#     print(value)

# dict = {1 : 'one' , 2 : 'two'}
# num1 = int(input())
# num2 = int(input())
#
# try:
#     value = 10/num1
#     value2= dict[num2]
# # except (ZeroDivisionError, KeyError):
# #     print('error')
# # else:
# #     print(value,value2)
# except ZeroDivisionError as error1:
#     print(error1)
# except KeyError as error2:
#     print(error2)
# else:
#     print(value,value2)

# def add(first, second):
#     if not type(first) is int or not type(second) is int:
#         raise TypeError
#     return first + second
#
# try:
#     add('1',1)
# except TypeError:
#     print('not supported data type')