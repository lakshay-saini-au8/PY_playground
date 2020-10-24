def lcs(str1, str2, i, j):
    if i == len(str1) or j == len(str2):
        return 0
    if str1[i] == str2[j]:
        return 1 + lcs(str1, str2, i+1, j+1)
    else:
        return max(lcs(str1, str2, i, j+1), lcs(str1, str2, i+1, j))


str1 = "abedgjc"
str2 = "bmdgsc"
ans = lcs(str1, str2, 0, 0)
print(ans)
