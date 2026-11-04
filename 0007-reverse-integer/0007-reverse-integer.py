class Solution:
    def reverse(self, x: int) -> int:
        places, finalResult = 0, 0

        if x < 0:
            isNegative = True
            x = x * -1
        else: isNegative = False
        
        currentNum = x
        while True:
            places += 1
            if (x - 10**places) < 0:
                break
                
        exponent = places
        while currentNum >= 10:
            divTen = currentNum // 10
            divTen = divTen * 10
            divTen = currentNum - divTen 
            currentNum = currentNum // 10
            finalResult += divTen * (10**(exponent-1))
            exponent -= 1
        finalResult += currentNum

        if isNegative: finalResult = finalResult * -1

        if finalResult > (2**31) - 1 or finalResult < (-2**31):
            return 0
        else:
            return finalResult
