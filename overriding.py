class Animal: # parent
    def toString(self):
        print("Animal")

class Monkey(Animal): # child

    def toString(self):
        print("monkey")

a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString() # monkey calls overridng methods

