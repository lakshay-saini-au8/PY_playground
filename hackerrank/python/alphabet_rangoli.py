def print_rangoli(size):
    start = ord("a")-1
    # your code goes here

    for i in range(size):
        str_new = ""
        for j in range((size-i)*2-2):
            str_new = str_new+"-"
        for k in range(i+1):
            str_new = str_new + chr(start+(size-k))+"-"
        for m in range(i, 0, -1):
            str_new = str_new+chr(start+1+(size-m))+"-"
        for l in range((size-i)*2-2):
            str_new = str_new+"-"

        print(str_new[:-1])
    size = size - 1
    for i in range(size, 0, -1):
        str_new = ""
        for j in range((size-i)*2+2):
            str_new = str_new+"-"
        for k in range(i):
            str_new = str_new + chr(start+(size+1-k))+"-"
        for m in range(i-1, 0, -1):
            str_new = str_new+chr(start+1+(size+1-m))+"-"
        for l in range((size-i)*2+2):
            str_new = str_new+"-"

        print(str_new[:-1])


print_rangoli(5)
