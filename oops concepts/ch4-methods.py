#This chapter explains different types of methods like Class, Instance and Static methods
#Class method can access and modify the class state.
#Static Method cannot access or modify the class state - as these methods do not take any cls argument at delcaration

class Student:

    school = 'High school'

    def __init__(self, sub1, sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def avg(self):
        return (self.sub1 + self.sub2 + self.sub3)/3

    @classmethod
    def getschool(cls):      #this method takes cls as argument
        return cls.school

    @staticmethod
    def getinfo():           #this method does not take any default argument
        print('This is student class and it cannot access self.sub1 or cls.school values')


s1 = Student(45, 55, 65)
s2 = Student(28, 32, 45)

#instance object access through self argument
print(s1.avg())
#class object access through cls argument
print(Student.getschool())
#static methods do not take any default arguments, it can be access with both instance and class objects
Student.getinfo()
s2.getinfo()

s1.school = 'New school'
print(s1.school)
print(s1.getschool())
print(s2.getschool())