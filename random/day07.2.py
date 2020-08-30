# given a string print vowel in it

def check_vowel(ch):
    vowel = ["a", "e", "i", "o", "u"]
    return ch in vowel


string = input("Enter your string:")

for sch in string:
    cond = check_vowel(sch)
    if cond:
        print(sch)
