class Solution:
    def intToRoman(self, num: int) -> str:
        if not num: 
            return

        out = ''

        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        Roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]

        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                out += Roman[i]
        return out
