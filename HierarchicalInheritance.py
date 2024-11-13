class student:
    def display(self):
        print("Parent class is student.")
    
class dept(student):
    def display2(self):
        print("Department of students.")
    
class domain(student):
     def display3(self):
        print("Domain of students.")

class age(student):
    def display4(self):
        print("Age of students.")

ob1=dept()
ob2=domain()
ob3=age()

ob1.display()
ob1.display2()
ob2.display3()
ob3.display4()