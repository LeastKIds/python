import user
# from user import *    # 다 불러올 시 _내용을 못불러옴

print(user.hello())
print(user.defaultUser.hello())
myUser = user.User()
print(myUser.hello(user.defaultName))

print(user._merge('a','b'))
print(user._value)