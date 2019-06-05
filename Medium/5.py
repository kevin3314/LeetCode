class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # Initialize
        l = [[False for j in range(len(s))] for i in range(len(s))]
        max_len = 1
        start = 0
        end = 0

        for i in range(len(s)-1):
            l[i][i] = True
            if s[i] == s[i+1]:
                l[i][i+1] = True
                max_len = 2
                start = i
                end = i+1

        l[len(s)-1][len(s)-1] = True

        for i in range(2, len(s)):
            for n in range(0, len(s)-i):
                l[n][i+n] = (l[n+1][i+n-1] and (s[n] == s[n+i]))
                if l[n][i+n]:
                    if i+1 > max_len:
                        max_len = i+1
                        start = n
                        end = i+n

        return s[start:end+1]


def main():
    sol = Solution()
    print(sol.longestPalindrome("abccba"))


if __name__ == "__main__":
    main()
