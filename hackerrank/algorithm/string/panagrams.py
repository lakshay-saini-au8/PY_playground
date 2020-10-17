# Complete the pangrams function below.
def pangrams(s):
    list_check = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
                  "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    for i in s:
        if i.lower() in list_check:
            list_check.remove(i.lower())
    if len(list_check) == 0:
        return "pangram"
    else:
        return "not pangram"
