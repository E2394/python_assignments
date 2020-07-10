strnumber= input("Enter a positive integer number..:")

while not strnumber.isnumeric():
    print("False entry!")
    strnumber = input("Enter a positive integer number..:")

power = len(strnumber)
number = int(strnumber)
strnumberlist = list(strnumber)
intnumberlist = list(range(power))
n = 0

print(strnumberlist)

for i in range(0,power):
    intnumberlist[i] = int(strnumberlist[i])
    n+= intnumberlist[i]**power
    i+= 1
    
if number == n:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is NOT an Armstrong number. The value of the control variable is {n}.")