# list = [0,1,2,3,4,5,6,7,8,9]
# print(list)
# del list[:3]
# print(list)
# del list[2:5]
# print(list)
#
# list = [0,1,2,3,4,5,6,7,8,9]
# print(list)
# list[1:6] = [100,200]
# print(list)

# list = [0,1,2,3,4,5,6,7,8,9]
# # print(list[:-3])
# # print(list[-5:])
#
# print(list[::-1])
# print(list[8:3:-1])
# print(list[-2:-4:-1])

# str = input()
# print(str[:3] + str[-3:])

# capitals = {'Korea' : 'Seoul', 'UK' : 'London'}
# print(capitals['Korea'])
# capitals['Japan'] = 'Tokyo'
# print(capitals)
#
# capitals.update({'USA' : 'Washington, D.C', 'China' : 'Beijing'})
# print(capitals)
# del capitals['USA']
# print(capitals)

set1 = set([1,2,3,4])
set2 = {(1,2),2,3,'Hello'}
print(set1)
set1.add(5)
print(set1)
set1.add(1)
print(set1)
set1.remove(4)
print(set1)
set1.update([7,8])
print(set1)
print(set1 & set2)
print(set1 | set2)
print(set1-set2)