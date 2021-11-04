# class Student:
#     def __init__(selfself, name):
#         print(name)
#
# s1 = Student('ABC')
#

# class Student:
#     def __init__(self):
#         pass
#     def say_hello(self):
#         print('Hello')
#
# s1 = Student()
# s1.say_hello()

# class MyClass:
#     def say_hello(self):
#         print('hello')
# m = MyClass()
# MyClass.say_hello(m)

# class Student:
#     def __init__(self, name):
#         pass
#     def say_hello(self):
#         print('Hello')
#
#     @classmethod
#     def create_student(cls, name):
#         return cls(name);
#
# s1 = Student.create_student('ABC')
# s1.say_hello()

# class Circle:
#     def __init__(self, x=0, y=0, r=1):
#         self.x=x
#         self.y=y
#         self.r=r
#
#     def __del__(self):
#         print('delete Circle')
#     def __repr__(self):
#         return 'circle'
#     def __add__(self, other):
#         return self.x + other.x, self.y + other.y
#     def __sub__(self, other):
#         return self.x - other.x, self.y - other.y
#     def __eq__(self, other):
#         if self.r == other.r and self.x == other.x and self.y == other.y:
#             return True
#         else:
#             return False
#
# c1 = Circle()
# c2 = Circle(1,1,2)
#
# print(c1, c2)
# print(c1 + c2, c1 - c2)
# print(c1 == c2)

# print(dir())
# class Student:
#     def __init__(self, name):
#         pass
#     def say_hellp(self):
#         print('Hello')
#
#     @classmethod
#     def create_student(cls, name):
#         return cls(name);
#
# print(dir())
# print(dir(Student))

# class MyClass:
#     message = 'hello'
#     def __init__(self, name):
#         self.name=name
#
# print(id(MyClass.message))
# a=MyClass('a')
# print(a.name, id(a.name), a.message, id(a.message))
# b=MyClass('b')
# print(b.name, id(b.name), b.message, id(b.message))
# MyClass.message = 'bye'
# print(a.message, b.message)

# class MyClass:
#     str = 'hello'
#
# a=MyClass()
# b=MyClass()
# MyClass.str = 'bye'
# print(a.str, b.str)
# a.str='a'
# print(id(MyClass.str), id(a.str), id(b.str))

# class MyArrClass:
#     arr=[1,2,3]
#
# c=MyArrClass()
# d=MyArrClass()
# MyArrClass.arr.append(4)
# print(c.arr, d.arr)
# c.arr.append(5)
# print(c.arr, d.arr)
# print(id(MyArrClass.arr), id(c.arr))

# class User:
#     def __init__(self, name = 'user'):
#         self.name = name,
#         self.address = '',
#         self.email = '',
#         self.phone = ''
#
# user = User()
# user2 = User('a')
# print(user.name)
# print(user2.name)

# class Member:
#     def __init__(self):
#         self.memberid='0'
#     def __repr__(self):
#         return 'memberid=' + self.memberid
#
# class Student(Member):
#     pass
#
# s = Student()
# m = Member()
# print(s)

class Member:
    def __init__(self):
        self.memberid = '0'
    def __repr__(self):
        return 'memberid=' + self.memberid

class Student(Member):
    def __init__(self, major='computer'):
        super().__init__();
        self.major = major
    def __repr__(self):

        return super().__repr__() + '\nmajor=' + self.major

s = Student()
# print(s.memberid)
# print(s.major)
print(s)

