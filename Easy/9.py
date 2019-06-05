class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = str(x)
        rev = tmp[::-1]
        return tmp == rev
