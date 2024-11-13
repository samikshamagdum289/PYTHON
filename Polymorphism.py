print(len("Samiksha"))
print(len([10,20,30]))

def add(x,y,z=0):
    return x+y+z

print("Addition is as follows:")
print(add(4,6))
print(add(3,5,8))


class S1:
    def name(self):
        print("My name is Samiksha Shankar magdum.")

    def age(self):
        print("my Age is 21.")

    def place(self):
        print("I am Live in kalamba.")


class S2:
    def name(self):
        print("My friend name is Samruddhi Dipak mithari.")

    def age(self):
        print("her age is 22.")

    def place(self):
        print("She Lives in Kale.")

ob1=S1()
ob2=S2()

for info in (ob1,ob2):
    info.name()
    info.age()
    info.place()


