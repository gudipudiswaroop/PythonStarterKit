#This chapter explains how method overloading and method overridding can be achieved with python


class A:

    def __init__(self):
        print('init method of A')

    def execute(self):
        print('A method executing')

class B(A):

    def __init__(self):
        print('init method of B')

    def execute(self):
        print('B method executing as method overloading')

class C(A):

    def __init__(self):
        print('init method of B')

    def execute(self, message):
        print('C method executing with message as', message)


b = B()
b.execute()

c = C()
c.execute('this is a c class method overridding')