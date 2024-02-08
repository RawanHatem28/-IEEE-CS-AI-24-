# problem 7
num = int(input())
divisor = 2
prime_factors =[]
while divisor <= num:
    if num % divisor == 0:
            prime_factors.append(divisor)
            num /= divisor
    else:
        divisor += 1
unique_prime_factors = list(set(prime_factors))
print(unique_prime_factors)