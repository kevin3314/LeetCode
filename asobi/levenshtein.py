def levenshtein(s1, s2):
    # any of string is empty
    if not s1 or not s2:
        return 0

    n, m = len(s1), len(s2)

    dp = [ [0 for j in range(m+1)] for i in range(n+1) ]

    for i in range(n+1):
        dp[0][i] = i

    for j in range(m+1):
        dp[j][0] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            # if character now looking at is same, cost = 0; otherwise 1
            cost = 0 if s1[i-1] == s2[j-1] else 1

            dp[i][j] = min( dp[i-1][j] + 1,
                            dp[i][j-1] + 1,
                            dp[i-1][j-1] + cost)

    print(dp)
    return dp[n][m]

if __name__ == "__main__":
    print(levenshtein("kitten", "kitten"))
