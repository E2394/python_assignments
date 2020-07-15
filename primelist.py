# For theory (primality test), check out https://en.wikipedia.org/wiki/Primality_test

number= int(input("Enter a number..:"))
primes = []

# Outer for loop begins with 2 because 1 is NOT prime.
# https://blogs.scientificamerican.com/roots-of-unity/why-isnt-1-a-prime-number/

for x in range(2,number+1): 
    root = x**(1/2)
    rootint = round(root)
    divisors = []
    for i in range(2,rootint+1):
        if (x % i) == 0:
            divisors.append(i)
        i+=1
    if not bool(divisors):
        primes.append(x)
    x+=1
    
print(primes)