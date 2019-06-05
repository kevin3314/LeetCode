class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = False

        if numRows == 1:
            return s

        rows = [[] for i in range(0, numRows)]
        now_row = 0
        for c in s:
            rows[now_row].append(c)
            if now_row == 0 or now_row == numRows -1:
                direction = not direction
            if direction:
                now_row += 1
            else:
                now_row -= 1

        res = ""
        for i in range(0,numRows):
            for c in rows[i]:
                res += c
        return res
            
def main():
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 4))

if __name__ == "__main__":
    main()
