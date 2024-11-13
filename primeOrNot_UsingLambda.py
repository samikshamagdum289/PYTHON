My_list = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

primes = list(filter(lambda x: x > 1 and all(x % i for i in range(2, int(x**0.5) + 1)), My_list ))
print("From the Given list ,The prime numbers are:",primes)

#OUTPUT:
#From the Given list ,The prime numbers are: [5, 7, 97, 23, 73, 61]