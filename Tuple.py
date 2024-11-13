T=("Mango","Samiksha","kiwi",True,45)
print(type(T))
print(T)
print(T[1])
print(T[1:4])
print(T[-3:-1])



#Change Tuple using type casting to list
x=list(T)
print(type(x))



x.insert(1,"Potato")
print(x)
x.remove("kiwi")
print(x)

#Convert a modified list into Tuple
T=tuple(x)
print(type(T))
print(T)