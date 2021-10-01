# list = [None for i in range(10)]
# print(list[0])
#
# def push(var):
#     for i in range(9,-1,-1):
#         if list[9] != None:
#             print("stack overflow")
#             break
#
#         elif list[i] != None:
#             list[i+1] = var
#             break
#         elif i==0:
#             list[0] = var
#             break
#
#
# def pop():
#     if list[0] == None:
#         return 'stack empty'
#     for i in range(9,-1,-1):
#         if i < 1:
#             result = list[0]
#             list[0] = None
#             return result
#         elif list[i] != None:
#             result = list[i]
#             list[i] = None
#             return result
#
# for i in range(0,11):
#     push(i)
#     print(list)
#
# for i in range(0,11):
#     print(pop())
#     print(list)


# font = -1
# rear = -1
# list = [None for i in range(10)]
# def put(var):
#     global rear
#     if rear < 9:
#         rear +=1
#         list[rear] = var
#         return list
#     else:
#         return None
#
# def get():
#     global rear
#     if rear >= 0:
#         result = list[rear]
#         del list[rear]
#         rear -=1
#         print(list)
#         return result
#     else:
#         return None
#
# for i in range(11):
#     print(put(i))
#
# print('-------------------')
# for i in range(11):
#     print(get())

# list = [1,3,6,9,12,15,18,21]
# length = len(list)
#
# def find(var):
#     global length
#     while True:
#         length = length//2
#         if length == 2:
#             if list[0] == var:
#                 return True
#             elif list[1] == var:
#                 return True
#             else:
#                 return False
#         elif list[length] == var:
#             return True
#         elif list[length] > var:
#             continue
#         elif list[length] < var:
#             for i in range(length):
#                 del list[i]
#             continue
#
#
# def binarySearch(var):
#     global length
#     low = 0
#     high = length - 1
#
#     while True:
#         if low > high:
#             return False
#         mid = (low + high) // 2
#         if list[mid] == var:
#             return True
#         elif list[mid] > var:
#             high = mid - 1
#             continue
#         elif list[mid] < var:
#             low = mid + 1
#     return False
#
# print(binarySearch(18))

list = [1,3,5,6,2,4,7,8]

def merge(list1, list2):
    result = []
    while True:
        if len(list1) == 0:
            result.extend(list2)
            break
        elif len(list2) == 0:
            result.extend(list1)
            break
        elif list1[0] < list2[0]:
            result.append(list1[0])
            del list1[0]
        elif list2[0] < list1[0]:
            result.append(list2[0])
            del list2[0]

    return result

def merge_sort(list):
    if len(list) == 1:
        return list

    list1 = merge_sort([list[i] for i in range(0, len(list) // 2)])
    list2 = merge_sort([list[i] for i in range(len(list)//2, len(list))])
    merge(list1, list2)

print(merge_sort(list))

print([list[i] for i in range(len(list)//2, len(list))])