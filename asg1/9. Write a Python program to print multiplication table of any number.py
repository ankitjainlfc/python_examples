# Write a Python program to print multiplication table of any number

num = int(input('Please enter a number: '))
count = int(input('Please enter a number by which table is needed: '))
i = 1
a = 0
while i <= count:
    a = num*i
    print(num, '*', count, '=: ', a)
    i = i+1

