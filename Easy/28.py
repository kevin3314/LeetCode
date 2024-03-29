class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # when needle is empty
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("hello", "ll"))
