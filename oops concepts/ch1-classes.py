#This chapter shows how classes are declared and objects are instantiated
#Multipe classes can be defined inside one file


class Python:

    def getName(self):
        print('this is a python class')


class Java:

    def getname(self):
        print('this is a java class')


obj1 = Python()
obj1.getName()

obj2 = Java()
obj2.getname()