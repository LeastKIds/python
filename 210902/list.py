# list = []
# list2 = [1,2,3,True,False]
# list3 = [(1,2,3), {'name' : 'user'}, [1,2,3]]
# list4 = [list, list2]
# print(list, list2)
# print(list3)
# print(len(list4), list4)

# list = [1,2,3,4,5]
# print(list[2], list[3])

# list = [0,1,25,3,4,5,2]
# print(list.index(2))
# list.insert(3,-1)
# print(list)
# list.append(6)
# print(list)
# list.extend([7,8])
# print(list)
# list.sort()
# print('sort', list)
# list.sort(reverse=True)
# print('reverse sort', list)
# list.reverse()
# print('reverse', list)

# list = [1,2,3,4,5]
# list.insert(0,6)
# list.append(0)
# print(list)
# list.sort()
# print(list)

# list = [1,2,3,4,5]
# del list[1]
# print(list)
# list.remove(1)
# print(list)

# list = [1,2,3,4,5]
# value = int(input())
# list.remove(value)
# print(list)

# list = [0,1,2,3,4,5,6,7]
# print(list[len(list)-1])
# print(list[-1])

# rect = (10,10,100,100)
# rect2 = 20,20,50,50
#
# print(type(rect), type(rect2))
# print(rect[1])
# print(rect2)
#
# first = 'Hello "YOU"'
# second = "Hello 'You'"
# multi1 = '''Hello
# friend'''
# multi2 = """Hello
# Friend"""
#
# print(first, second)
# print(first[0], second[0])
# print(multi1)
# print(multi2)

# str = 'hello my friend'
# split_default = str.split()
# split_char = str.split('e')
# print(split_default)
# print(split_char)
#
# str_list = list(str)
# print(str_list)
#
# joined_empty = ''.join(str_list)
# joined_char = '-'.join(str_list)
# print(joined_empty)
# print(joined_char)

# list = [0,1,2,3,4,5,6,7,8,9]
# sub1 = list[5:8]
# sub2 = list[7:]
# sub3 = list[:4]
# sub4 = list[::2]
# print(sub1)
# print(sub2)
# print(sub3)
# print(sub4)

# list = [0,1,2,3,4,5,6,7,8,9]
# print(list[:-3])
# print(list[-5:])
#
# list = [0,1,2,3,4,5,6,7,8,9]
# print(list[::-1])
# print(list[8:3:-1])
# print(list[-2:-4:-1])

list = [0,1,2,3,4,5,6,7,8,9]
print(list)
del list[:3]
print(list)
del list[2:5]
print(list)

list = [0,1,2,3,4,5,6,7,8,9]
print(list)
list[1:6] = [100,200]
print(list)