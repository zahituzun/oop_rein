# class Footballer(object):
#     football_club = "barcelona"
#     age = 30
#
# f1 = Footballer()
#
# print(f1.age)
# print(f1.football_club)
#
# class Square(object):
#     edge = 5 #metre
#
#     def area(self):
#         area = self.edge * self.edge
#         print("Area:", area)
#
# s1 = Square()
# print(s1)
# print(s1.edge)
# s1.area()





#-------------------------------------------------------------------------






# class Emp(object):
#     age = 25
#     salary = 1000
#     def agesalartRatio(self):
#         a = self.age / self.salary
#         print("method:", a)
# #function
# def ageSalaryRatio(age,salary):
#     print("function:", age / salary)
# e1 = Emp()
# e1.agesalartRatio()
#
# ageSalaryRatio(30,3000)
# def FindArea(a,b):
#     area = a*b**2
#     #print(area)
#     return area
# pi = 3.14
# r = 5
# result1 = FindArea(pi,r)
# result2 = FindArea(pi,10)
# print(result1 + result2)



#--------------------------------------------------------------------------




# initializer or constractor




#
class Animal(object):



    def __init__(self,name,age):
        self.name = name
        self.age = age


    def getAge(self):
        return self.age

    def getName(self):
        print(self.name)

a1 = Animal("dog", 2)
a2 = Animal("cat", 4)
a3 = Animal("bird", 6)

a1.getName()
print(a1.getAge())
