# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def Age(self):
#         return self.age
#
#     @Age.setter
#     def Age(self, age):
#         if isinstance(age, int):
#             self.age = age
#         else:
#             raise ValueError
#
#     @Age.deleter
#     def Age(self):
#         print('delete age data!')




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def get_age(self):
        return self.age


    def set_age(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError

    def delete_age(self):
        print('delete age data!')

    Age = property(get_age, set_age, delete_age, "age")

p = Person('Bob', 45)
print(p.Age)
p.Age = 10
print(p.Age)
del p.Age
print(p.age)