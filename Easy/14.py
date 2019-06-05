class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        tmp = ""

        if not strs:
            return ""

        for i in range(min(map(lambda x: len(x), strs))):
            s_list = [s[i]for s in strs]
            t_list = list(filter(lambda x: x == s_list[0], s_list))
            if len(s_list) == len(t_list):
                tmp += s_list[0]
            else:
                break

        return tmp
