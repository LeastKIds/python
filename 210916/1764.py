# a, b = map(int, input().split())
#
# setA = set()
# setB = set()
# for i in range(a):
#     setA.add(input())
#
# list = []
# for i in range(b):
#     setB.add(input())
#
# list = setA & setB
# print(len(list))
# for i in sorted(list):
#     print(i)

import sys

a, b = map(int, sys.stdin.readline().split())

setA = set()
setB = set()
for i in range(a):
    setA.add(sys.stdin.readline())

list = []
for i in range(b):
    setB.add(sys.stdin.readline())

list = setA & setB
print(len(list))
# for i in sorted(list):
#     print(i)
print(sorted(list))