import math
def sum_of_primes(n):
    if n==1: return 0
    primes = [2]
    num = 3
    while num <= n:
        i = 0
        while i<len(primes) and primes[i]<=math.floor(num**0.5):
            if num%primes[i]==0:
                break
            i+=1
        else:
            primes.append(num)
        num += 2
    return sum(primes)