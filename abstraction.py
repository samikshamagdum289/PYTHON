from abc import ABC,abstractmethod
class car(ABC):
    def mileage(self):
        pass

class Tesla (car):
    def mileage(self):
        print("The mileage is 30 kmph")
    
class Renault (car):
    def mileage(self):
        print("The mileage is 35 kmph")

class TATA (car):
    def mileage(self):
        print("The mileage is 40 kmph")

class Duster (car):
    def mileage(self):
        print("The mileage is 25 kmph")

class Suzuki (car):
    def mileage(self):
        print("The mileage is 45 kmph")

#Driver code
t=Tesla()
t.mileage()

r=Renault()
r.mileage()

t1=TATA()
t1.mileage()

d=Duster()
d.mileage()

s=Suzuki()
s.mileage()    