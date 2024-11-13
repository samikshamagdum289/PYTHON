class student:
    def display(self):
        print("Parent class is student.")
    
class faculty:
    def display2(self):
        print("Parent class is faculty")
    
class domain(student,faculty):
     def display3(self):
        print("Derived form student and faculty.")

ob=domain()

ob.display()
ob.display2()
ob.display3()