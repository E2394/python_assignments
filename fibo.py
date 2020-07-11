# In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence,
# called the Fibonacci sequence, such that each number is the sum of the two 
# preceding ones, starting from 0 and 1.

fibo = [0, 1]

head = 0
i = 0

while head < 55:
    head = fibo[i] + fibo[i+1]
    fibo.append(head)
    i+=1
print(fibo)