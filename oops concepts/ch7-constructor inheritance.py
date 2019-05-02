#This chapter explains the inheritance from constructors


class A:

    def __init__(self):
        print('init of A class')

    def features1(self):
        print('Feature1 from A is working')

    def features2(self):
        print('Feature2 is working')

class B(A):

    #if a constructor in sub class is not defined, on object instantiation, the object will try to call parent class

    def features3(self):
        print('Feature3 is working')


class C(A):

    #if a constructor in sub class is defined, the object will do not call the parent constructor

    def __init__(self):
        print('init of C class')

    def features3(self):
        print('Feature3 is working')


class D(A):

    #if a constructor in sub class is defined, the sub class can access the parent class methods through super

    def __init__(self):
        super().__init__()
        print('init of D class')

    def features3(self):
        print('Feature3 is working')

class E:

    def __init__(self):
        print('init of E class')

    def features4(self):
        print('Feature4 is working')

class F(A,E):

    def __init__(self):
        super().__init__()
        print('F init')


obj = A()
obj.features2()

obj1 = B()
obj1.features3()

obj2 = C()
obj2.features1()
obj2.features3()

obj3 = D()

obj4 = F()