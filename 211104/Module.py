# import random
#
# value = random.random()
# print(value)

# import random as rd
#
# value = rd.random()
# print(value)

# from random import random
#
# value = random()
# print(value)

# from random import random as rd
#
# value = rd()
# print(value)

# import sys
#
# print(sys.argv)
# sys.stdout.write('hello')
# sys.stderr.write('error\n')

# import os
# print(os.name)
# print(os.getcwd())
# # os.system('notepad')  # 맥은 안 됨 ㅠㅠ

# import math
# import random
# import statistics as st
#
# print('log', math.log(8,2))
# print('pi', math.pi)
#
# print('sample', random.sample(range(100), 10))
# print('rand float', random.random())
# print('rand int', random.randint(10,100))
# data=[i for i in range(1,11)]
# data.append(100)
# print('choice', random.choice(data))
#
# print('mean', st.mean(data))
# print('median', st.median(data))
# print('variance', st.variance(data))
# print('stdev', st.stdev(data))

def func():
    return 'func called'

# if __name__ == '__main__':
print(func())