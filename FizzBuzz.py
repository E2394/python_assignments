numbers = list(range(1,101))
for i in numbers:
    if i%3 == 0 and i%5 == 0:
        numbers[i-1]="FizzBuzz" 
    elif i%3 == 0 and i%5 !=0:
        numbers[i-1]="Fizz"
    elif i%3 !=0 and i%5 ==0:
        numbers[i-1]="Buzz"
    else:
        numbers[i-1]=i
    print(numbers[i-1])
    i+=1
