# Write a Python program to find sum of all natural numbers between 1 to n.

num = int(input('Please enter a number: '))
sum = 0
i = 1

while i <= num:
    sum = sum + i
    i = i+1

print('Sum of numbers till %d is: %d' %(num,sum))
