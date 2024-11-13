num = int(input("Enter a number: "))
print("The even numbers up to", num, "are:")
sum = 0

for i in range(2, num + 1):
    if i % 2 == 0:
        print(i)
        sum = sum + i

print("\nAddition of even numbers is:", sum)
