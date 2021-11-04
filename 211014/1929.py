num1, num2 = map(int, input().split())

list = [i for i in range(num2+1)]

for i in list:
    if i == 1:
        list[1]=0
        continue
    if i != 0:
        for j in range(i*2, num2+1, i):
            list[j] = 0



for i in list:
    if i >= num1:
        print(i)


