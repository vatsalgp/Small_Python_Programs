import math
def nthPrime(n):
    primes = [2]
    num = 3
    while len(primes)< n:
        i = 0
        while i<len(primes) and primes[i]<=math.floor(num**0.5):
            if num%primes[i] ==0:
                break
            i+=1
        else:
            primes.append(num)
        num += 1
    return primes[-1]

inp = int(input("Enter the order of Prime:"))
print(f"The {inp}th prime is {nthPrime(inp)}")