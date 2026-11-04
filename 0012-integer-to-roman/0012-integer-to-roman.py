class Solution:
    def intToRoman(self, num: int) -> str:
        conversion = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        result = []
        numbers = list(conversion.keys())
        numbers.reverse()
        count = 0
        while num > 0:
            indx = 0
            num, rest = divmod(num, 10)
            rest *= 10**count
            
            for i in range(len(numbers)):
                if numbers[i] <= rest:
                    while rest >= numbers[i]:
                        result.insert(indx, conversion[numbers[i]])
                        rest -= numbers[i]
                        indx+=1
                    if rest == 0: 
                        count += 1
                        break
            else: count+=1   
        return "".join(result)