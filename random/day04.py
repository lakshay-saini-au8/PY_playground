# question
'''
Subjects are s1,s2,s3,s4,s5
Write a program that takes input from the user as marks in 5 subjects and assigns a
grade according to the following rules:
Perc = (s1+s2+s3+s4+s5)/5
A, if Perc is 90 or more
B, if Perc is between 70 and 90(not equal to 90)
C, if Perc is between 50 and 70(not equal to 90)
D, if Perc is between 30 and 50(not equal to 90)
E, if Perc is less than 30
'''

s1 = int(input("Enter marks for first subject:- "))
s2 = int(input("Enter marks for second subject:- "))
s3 = int(input("Enter marks for third subject:- "))
s4 = int(input("Enter marks for fourth subject:- "))
s5 = int(input("Enter marks for fifth subject:- "))

percentage = ((s1+s2+s3+s4+s5)/5)

if percentage < 30:
    print("E")
elif percentage >= 30 and percentage < 50:
    print("D")
elif percentage >= 50 and percentage < 70:
    print("C")
elif percentage >= 70 and percentage < 90:
    print("B")
else:
    print("A")
