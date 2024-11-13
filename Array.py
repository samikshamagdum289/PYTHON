import array as arr
a=arr.array('i',[1,2,3])
print("The 1st created array is :",end="")
for i in range (0,3):
    print(a[i],end="")

a.insert(1, 4)
print("\n1st Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")

print("\nElement at index a[0] is: ", a[0])
print("Element at index a[3] is: ", a[3])

b = arr.array('d', [2.5, 3.2, 3.3])
print("\nThe 2nd created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")

b.append(4.4)
print("\n2nd Array after insertion : ", end=" ")
for i in (b):
    print(i, end=" ")

print("\nElement at index b[1] is: ", b[1])
print("Element at index b[2] is: ", b[2])

print("original Array is:",*a)
a.reverse()
print("Reversed array:", *a)
