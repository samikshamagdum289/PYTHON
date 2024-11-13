num=int(input("Enter a number:"))
print("The natural numbers upto" ,num, "are:")
for i in range(1,num+1):
  print(i)

print("The reverse of natural numbers from" ,num, "are:")

for i in range(num - 1, 0, -1):
    print(i)

sum=0
while num > 0:
        sum += num
        num -= 1

print("Addition of natural number is:",sum)