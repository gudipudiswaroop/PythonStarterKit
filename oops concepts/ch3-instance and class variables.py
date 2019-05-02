#This chapter covers the difference between instance and class variables

class Language:

    type = 'programming language'

    def __init__(self):
        self.name = 'Python'
        self.mode = 'interpreter language'


lang1 = Language()
lang2 = Language()

lang2.name = 'java'
lang2.mode = 'compiled language'

print(lang1.name, lang1.mode, lang1.type)
print(lang2.name, lang2.mode, lang2.type)

#Modify class variable will affect all objects that are refering to a class
Language.type = 'some language'

print(lang1.name, lang1.mode, lang1.type)
print(lang2.name, lang2.mode, lang2.type)

#Modifing class variable through object will only affect the respective object variable

lang1.type = 'scripted language'

print(lang1.name, lang1.mode, lang1.type)
print(lang2.name, lang2.mode, lang2.type)




