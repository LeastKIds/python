import sys

r = int(sys.stdin.readline().rstrip())
result = []

for i in range(r):
    fnc = sys.stdin.readline().rstrip()
    list_len = int(sys.stdin.readline().rstrip())
    listL = sys.stdin.readline().rstrip()
    if list_len == 0:
        listL = []
    else:
        listL = listL[1:len(listL) - 1].split(',')
    errorE = True
    reverse = True

    for j in range(len(fnc)):
        if fnc[j] == 'R':
            if reverse == True:
                reverse = False
            else:
                reverse = True
        elif fnc[j] == 'D':
            if len(listL) == 0:
                result.append('error')
                errorE = False
                break
            if reverse:
                del listL[0]
            else:
                listL.pop()

        if j == len(fnc) -1 and len(listL) == 0:
            result.append('[]')
            errorE = False
            break

    if errorE:
        word = ''
        if reverse:
            for k in range(len(listL) - 1):
                word += listL[k] + ','
            word += listL[len(listL) - 1]
        else:
            for k in range(len(listL) - 1, 0, -1):
                word += listL[k] + ','
            word += listL[0]
        result.append('[' + word + ']')

for i in result:
    print(i)
