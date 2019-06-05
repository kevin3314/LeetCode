class Solution:
    def reverse(self, x: int) -> int:
        check = 1
        if x < 0:
            x = -x
            check = -1
        tmp = str(x)
        tmp = tmp[::-1]
        if len(tmp) == 1:
            return check * int(tmp)
        
        while tmp[0] == "0":
            tmp = tmp[1:len(tmp)]

        if check * int(tmp) > 2**31-1 or check * int(tmp) < -2**31:
            return 0
        return check * int(tmp)

