# Count No of Primes upto N
def count_primes(till):
    primes=[2]
    if(till<2):
        return 0
    elif(till==2):
        return 1
    for num in range (3,till+1,2):
        i=0
        while (i<len(primes) and primes[i]<=num**0.5):
            if num%primes[i]==0:
                break
            i+=1
        else:
            primes.append(num)
    return len(primes)

till = int(input("Find the no of Primes upto: "))
print("There are " + str(count_primes(till)) + " Primes till " + str(till))