a = input()

arr = [i.upper() for i in a]
result = {}
for a in arr:
    result[a] = 0

for a in arr:
    result[a] += 1

max = 0
maxA = ''
for r in result:
    if result[r] > max:
        max = result[r]
        maxA = r

count = 0
for r in result:
    if result[r] == max:
        count += 1

if count >= 2:
    print('?')
else:
    print(maxA)