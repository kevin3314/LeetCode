class Solution:
    def isValid(self, s: str) -> bool:
        left_list = ["(", "{", "["]
        right_list = [")", "}", "]"]

        stack = []
        
        if not s:
            return True

        for c in s:
            if c in left_list:
                stack.append(c)
            elif c in right_list:
                try:
                    c2 = stack.pop()

                    # that index of c is equal index of c2 means corresponding mark
                    if left_list.index(c2) != right_list.index(c):
                        return False

                except:
                    return False
            else:
                return False

        # When all sign are passed, if stack has any element, then false; otherwise true
        if stack:
            return False

        return True


if __name__ == "__main__":
    cls = Solution()
    print(cls.isValid("{}"))
