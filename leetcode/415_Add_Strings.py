# question  https://leetcode.com/problems/add-strings/
# solution
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = self.strToInt(num1)
        n2 = self.strToInt(num2)
        return str(n1+n2)

    def strToInt(self, s):
        num = 0
        for ch in s:
            ch_to_int = ord(ch)-ord("0")
            num = num*10+ch_to_int
        return num
