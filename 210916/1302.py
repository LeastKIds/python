num = int(input())
book = []
for i in range(num):
    book.append(input())

result = {}
for b in book:
    result[b] = 0

for b in book:
    result[b] += 1
max = 0
for r in result:
    if result[r] > max:
        max = result[r]

list = []
for r in result:
    if result[r] == max:
        list.append(r)
        
print(sorted(list)[0])
#
# if count >= 2:
#     print('?')
# else:
#     print(maxA)