#This chapter explains the inner class concept and ways to access the inner class

class Language:

    def __init__(self, name, mode, type):
        self.name = name
        self.mode = mode
        self.type = self.Type(type)

    def show(self):
        print('{} is a {} language of type {}'.format(self.name, self.mode, self.type.show()))


    class Type:

        def __init__(self, type):
            self.type = type

        def show(self):
            return self.type


#1-use Access the inner class through upper class using constructor
lang1 = Language('python', 'scripting', 'interpreter')
lang2 = Language('java', 'programming', 'compiled')

lang1.show()
lang2.show()

#2-use Access the inner class directly independent of upper class
type1 = Language.Type('Language is of some type')

print(type1.show())

