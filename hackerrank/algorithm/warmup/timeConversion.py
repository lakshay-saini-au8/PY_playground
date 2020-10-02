def timeConversion(s):
    hh, mm, ss = s[0:len(s)-2].split(":")
    s_type = s[-2:]

    if s_type == "PM" and int(hh) != 12:
        hh = int(hh)+12
    if int(hh) == 12 and s_type == "AM":
        hh = '00'
    return f"{hh}:{mm}:{ss}"
