class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        value_dict = { "M": 1000,
                       "CM": 900,
                       "D":  500,
                       "CD": 400,
                       "C" : 100,
                       "XC":  90,
                       "L":   50,
                       "XL":  40,
                       "X":   10,
                       "IX":   9,
                       "V":    5,
                       "IV":   4,
                       "I":    1}
        tmp = s
        res = 0

        while tmp:
            if len(tmp) == 1:
                res += value_dict[tmp]
                break
            else:
                if tmp[0:2] in value_dict:
                    res += value_dict[tmp[0:2]]
                    tmp = tmp[2:]
                else:
                    res += value_dict[tmp[0]]
                    tmp = tmp[1:]

        return res
