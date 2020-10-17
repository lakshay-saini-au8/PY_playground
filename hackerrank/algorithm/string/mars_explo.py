def marsExploration(s):
    original_s = "SOS"*(len(s)//3)
    count = 0
    for i in range(len(s)):
        if s[i] != original_s[i]:
            count += 1

    return count
