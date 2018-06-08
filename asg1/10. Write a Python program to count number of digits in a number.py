# Write a Python program to count number of digits in a number.

n = int(input("Please enter a number: "))
div = 10
count = 1

while n % div != n:
    count = count + 1
    div = div * 10

print('Digits in the given number are: ', count)
