
from abc import ABC, abstractmethod
# abstract metod kullanmanın 2 kuralı var 1. si abstract metodu
#olan class tan nesne oluşturamassın
#2. olarak abstract class ta kullanılan herhangi bi metod
# benim subclasssım olan bir yerde kullanılmak zorundadır.
class Animal(ABC):

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def run(self):
        pass

class Bird(Animal):

    def __init__(self):
        print("bird")

    def walk(self):
        print("walk")


    def run(self):
        print("run")

b1 = Bird()

