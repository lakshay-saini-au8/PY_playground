'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

'''


def capitalize(str):
    seprate = str.split(" ")

    for index, word in enumerate(seprate):
        word = word[0].upper() + word[1:]
        seprate[index] = word

    print(" ".join(seprate))


capitalize("alison heck")
capitalize("chris alan")
