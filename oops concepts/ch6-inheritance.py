#This chapter explains how inheritance can be achieved in python


class A:

    def features1(self):
        print('Feature1 from A is working')

    def features2(self):
        print('Feature2 is working')

class B(A):

    def features3(self):
        print('Feature3 is working')

class C(B):

    def features4(self):
        print('Feature4 is working')

class D():

    def features1(self):
        print('Feature1 from D is working')

    def features5(self):
        print('Feature5 is working')

class E(D,A):

    def feature6(self):
        print('Feature6 is working')


b = B()
b.features1()

c= C()
c.features3()
c.features2()

e = E()
e.features1()
