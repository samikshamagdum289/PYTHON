max=lambda a,b,c: (a if (a > b and a  >c) else b if b > c else c)
print("max number is :",max(12,45,67))