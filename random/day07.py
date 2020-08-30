''' 
Q1. Write a user driven program which will will ask users to input two no and perform some
calculation
Eg
Input no 1: 5
Input no 2: 10
Enter 1 to do addition
Enter 2 to do subtraction
Enter 3 to do multiplication
Enter 4 to do division

'''
num1 = int(input("Enter your first no:- "))
num2 = int(input("Enter your second no:- "))
print(f"Enter 1 to do addition")
print(f"Enter 2 to do subtraction")
print(f"Enter 3 to do multiplication")
print(f"Enter 4 to do division")

option = int(input("Enter you choice:- "))
if(option == 1):
    print(f"{num1 + num2}")
elif(option == 2):
    print(f"{num1 - num2}")
elif(option == 3):
    print(f"{num1 * num2}")
else:
    print(f"{num1 / num2}")
