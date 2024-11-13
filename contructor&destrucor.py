class Demo:
    def __init__(self):  # constructor
        self.s = 10
        print("Value of s is:", self.s)
    
    def __del__(self):  # destructor
        print("Destructor is called.")

# Creating an instance of the class
ob = Demo()
