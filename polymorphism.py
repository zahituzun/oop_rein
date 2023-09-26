class Employee:

    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * raise_rate
        print(result)
class CompEng(Employee):

    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100 * raise_rate
        print(result)
class EEE(Employee):

    def raisee(self):
        raise_rate = 0.3
        result =  100 + 100 * raise_rate
        print(result)

e1 = Employee()

ce = CompEng()

eee = EEE()

Employee_list = [ce,eee]

for employee in Employee_list:
    employee.raisee()