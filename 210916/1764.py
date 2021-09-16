a, b = map(int, input().split())

setA = set()
setB = set()
for i in range(a):
    setA.add(input())

list = []
for i in range(b):
    setB.add(input())

list = setA & setB
print(len(list))
for i in sorted(list):
    print(i)