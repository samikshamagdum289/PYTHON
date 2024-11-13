class parent:
    def display(self):
        print("Parent class.")
    
class child(parent):                                 
    def display1(self):
        print("Child class")
ob= child() #Instace of a class
ob.display() 
ob.display1()