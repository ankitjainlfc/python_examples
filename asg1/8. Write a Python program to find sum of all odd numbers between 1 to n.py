# Write a Python program to find sum of all odd numbers between 1 to n

num = int(input('Please enter the number: '))

sum_a = 0
i = 1

while i <= num:
    if i % 2 != 0:
       sum_a = sum_a + i
    i = i+1
       
print('Sum of all odd numbers from 0 to %r is: %r' %(num,sum_a))
