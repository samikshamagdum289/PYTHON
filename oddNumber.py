num = int(input("Enter a number: "))
print("The odd numbers up to", num, "are:")
sum = 0

for i in range(1, num + 1):
    if i % 2 != 0:
        print(i)
        sum = sum + i

print("\nAddition of odd numbers is:", sum)
