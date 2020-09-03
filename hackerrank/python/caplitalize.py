'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

'''


def capitalize(str):
    seprate = str.split(" ")
    for index, word in enumerate(seprate):
        if (word != ''):
            word = word[0].upper() + word[1:]
        seprate[index] = word

    return " ".join(seprate)


print(capitalize("hello   world  lol"))
# capitalize("chris alan")
