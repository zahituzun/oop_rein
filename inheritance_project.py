class Website:

    def __init__(self, name, surname):
        self.name = name
        self. surname = surname

    def logInfo(self):
        print(self.name + " " + self.surname)

class Website1(Website):
    "child"
    def __init__(self, name, surname, ids):
        Website.__init__(self, name , surname)
        self.ids = ids
    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)


p2 = Website1("name","surname", "123")

p2.login()



