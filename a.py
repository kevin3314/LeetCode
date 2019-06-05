class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = ['']
        # "" なら0を返す
        if not s:
            return 0
        maxi = 1
        # 文字列を1文字目から最後まで見ていく。
        for i in range(0, len(s)):
            print(i)
            print(substrings)
            # その時点までの有効な部分文字列のリストの、それぞれの要素について調べる
            add_substrings_list = []
            rm_substrings_list = []
            for substring in substrings:
                # ""が調べる部分文字列なら、読んだ文字を部分文字列リストに加える
                if not substring:
                    add_substrings_list.append(s[i])
                # それ以外なら普通に処理
                else:
                    print("substring:" + substring)
                    print("s[i]:" + s[i])
                    # i番目の文字が部分文字列にすでに含まれていたら、その文字列をリストから削除する 長さが大きければ値を更新
                    if s[i] in substring:
                        if maxi < len(substring):
                            maxi = len(substring)
                    # 含まれていないなら後ろに読んだ文字を足してリストに追加する
                    else:
                        add_substrings_list.append(substring + s[i])
                        print("substring + s[i]:" + substring + s[i])
                    # どちらにしても読んでいる部分文字列はリストから取り除く
                    rm_substrings_list.append(substring)
            for rm_string in rm_substrings_list:
                substrings.remove(rm_string)
            substrings.extend(add_substrings_list)
        for substring in substrings:
            if len(substring) > maxi:
                maxi = len(substring)
        return maxi

def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstring("au"))


if __name__ == "__main__":
    main()
