# Enter your code here. Read input from STDIN. Print output to STDOUT
n  = input()
lowerCase = []
upperCase = []
odd = []
even = []

for i in n:
    if i.isdigit():
        num = int(i)
        if num % 2 == 0:
            even.append(str(num))
        else:
            odd.append(str(num))
    elif i.isupper():
        upperCase.append(i)
    elif i.islower():
        lowerCase.append(i)
lowerCase = "".join(sorted(lowerCase))
upperCase = "".join(sorted(upperCase))
odd = "".join(sorted(odd))
even = "".join(sorted(even))

print(lowerCase+upperCase+odd+even)
