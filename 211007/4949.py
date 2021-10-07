import sys

resultList = []
while True:
    list = []
    str = sys.stdin.readline().rstrip()
    if str == '.':
        break
    for i in range(len(str)):
        if str[i] == '.':
            if len(list) == 0:
                resultList.append('yes')
            else:
                resultList.append('no')
            break
        if str[i] == '(':
            list.append('(')
        elif str[i] == '[':
            list.append('[')
        elif str[i] == ')':
            if len(list) ==0:
                resultList.append('no')
                break
            elif list.pop() != '(':
                resultList.append('no')
                break
        elif str[i] == ']':
            if len(list) == 0:
                resultList.append('no')
                break
            elif list.pop() != '[':
                resultList.append('no')
                break

for i in resultList:
    print(i)