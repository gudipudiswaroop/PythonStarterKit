#This chapter shows how a constructor can be defined


class Python:

    def __init__(self):
        self.name = 'python'

    def getname(self):
        print('this is a {} class'.format(self.name))


class Java:

    def __init__(self, name):
        self.name = name

    def getname(self):
        print('this is a', self.name, 'class')   #dirty way of printing


obj1 = Python()
obj1.getname()

obj1 = Python()
obj1.name = 'java'
obj1.getname()

obj2 = Java('java')
obj2.getname()

