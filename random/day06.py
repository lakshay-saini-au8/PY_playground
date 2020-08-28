'''
Task 1 - Write a program to print all the prime numbers between 1 to 100.
Task 2 - Using range and for loop, print all multiples of 5, 7, 11 from 1 to 1001.
Task 3 - Take 10 integers from the keyboard using loop and print their average value.
'''

# Task 1

for i in range(2, 169):
    for j in range(2, i):
        if(i % j == 0):
            break

    else:
        print(i)


# Task 2
for i in range(1, 1002):
    if(i % 5 == 0 or i % 7 == 0 or i % 11 == 0):
        print(i)


# Task 3
marks = []
for i in range(10):
    number = int(input(f"Enter value {i+1}: "))
    marks.append(number)

average = sum(marks)/len(marks)
print(f"Average of all values is {average} ")
