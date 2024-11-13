Max = lambda a, b, c : (a if (a > b and a > c) else b if b > c else c)
print("Maximum number is :",Max(13, 26,31))

#OUTPUT:
#Maximum number is : 31