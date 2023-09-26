class Calc(object):
    def __init__(self,a,b):
        "initialize values"
        self.value1 = a
        self.value2 = b
    def Add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2
    def Multiply(self):
        "multiplication a*b = result -> return result"
        return self.value1 * self.value2
print("Choose add(1), multiply(2)")
selection = input("select 1 or 2")
v1 = int(input("first value"))
v2 = int(input("second value"))
c1 = Calc(v1,v2)
if selection == "1":
    add_result = c1.Add()
    print("Addition result:", add_result)
elif selection == "2":
    multiply_result = c1.Multiply()
    print("Multiplication result:", multiply_result)


#print("Add: {} , Multiply: {}".format(add_result,multiply_result))