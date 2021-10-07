import sys

n = int(input())
list = []

for i in range(n):
    n1 = int(sys.stdin.readline().rstrip())
    if n1 != 0:
        list.append(n1)
    else:
        list.pop()

result = 0
for i in list:
    result += i
print(result)