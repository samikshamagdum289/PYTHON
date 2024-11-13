#check prime or not using lambda function
prime = range(2, 20) 
for i in range(2, 8): 
     primes = filter(lambda x: x == i or x % i, prime)

print prime
