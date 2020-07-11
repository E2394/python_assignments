# for theory, check out https://en.wikipedia.org/wiki/Primality_test

number= float(input("Enter a number..:"))
root = number**(1/2)
rootint = round(root)
divisors = []

for i in range(2,rootint+1):
    if (number % i) == 0:
        divisors.append(i)
    i+=1

if not bool(divisors):
    print(f"{number} is prime.")
else:
    print(f"{number} is NOT prime.")