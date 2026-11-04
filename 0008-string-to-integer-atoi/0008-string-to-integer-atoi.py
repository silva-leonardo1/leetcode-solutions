class Solution:
    def myAtoi(self, s: str) -> int:
        finalResult = 0
        foundDigit = False 
        negative = False
        sign = 1
        
        for i in range(len(s)):
            if s[i] == "-" and foundDigit == False:
                foundDigit = True
                sign = -1
                continue 
            elif s[i] == "+" and foundDigit == False:
                foundDigit = True
                continue
            if s[i].isdigit():
                finalResult *= 10
                foundDigit = True
                finalResult += (ord(s[i]) - ord('0'))
            if (foundDigit == False and s[i] != " ") or (foundDigit == True and s[i].isdigit() == False):
                break
        
        finalResult *= sign
        if finalResult > (2**31) - 1:
            return (2**31) - 1
        elif finalResult < -(2**31):
            return -(2**31)
        else: return finalResult