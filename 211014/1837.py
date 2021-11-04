num, k = map(int, input().split())

list = [i for i in range(num+1)]
resultP = 0

for i in list:
    if i == 1:
        list[1]=0
        continue
    if i != 0:
        for j in range(i*2, num+1, i):
            list[j] = 0
        if 0 == num % i:
            resultP = num // i
            break

if resultP > k:
    print('GOOD')
else:
    print('BAD',resultP)

