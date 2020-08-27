input1 = int(input("Enter your first number: "))
input2 = int(input("Enter your second number: "))

Sub = input1-input2

print(f"address for input1 is {hex(id(input1))},address for input2 is {hex(id(input1))}, and subtraction of {input1} and {input2} is {Sub}")