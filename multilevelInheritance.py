class student:
    def display(self):
        print("Parent class.")
    
class dept(student):
    def display2(self):
        print("Intermeditory class.")
    
class domain(dept):
     def display3(self):
        print("Derived class.")

ob=domain()
ob.display()
ob.display2()
ob.display3()