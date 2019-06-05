class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_map = { "2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"],
                    "5": ["j", "k", "l"],
                    "6": ["m", "n", "o"],
                    "7": ["p", "q", "r", "s"],
                    "8": ["t", "u", "v"],
                    "9": ["w", "x", "y", "z"] }
        res = [""]

        if not digits:
            return []

        for s in digits:
            tmp = []
            if s in num_map:
                for x in res:
                    for number in num_map[s]:
                        tmp.append(x+number)
                res = tmp
            else:
                pass
        return res
