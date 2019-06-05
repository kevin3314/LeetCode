class Solution:
    def generateParenthesis(self, n):
        # define length of list
        list_len = 2*n

        tuples = []
        tuples.append(("(", 1))

        for i in range(1, list_len):
            new_tuples = []
            for t in tuples:
                # ( はどんな時でも付けれる
                new_tuples.append((t[0]+"(", t[1] +1))
               
                # ) は（の数が）の数より多い時だけ付けれる
                if t[1] > 0:
                    new_tuples.append((t[0]+")", t[1] -1))
            
            tuples = new_tuples

        res_pars = []
        for t in tuples:
            if t[1] == 0:
                res_pars.append(t[0])

        return res_pars

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
