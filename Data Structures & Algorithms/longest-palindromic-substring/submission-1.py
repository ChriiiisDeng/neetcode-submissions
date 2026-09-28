class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res_start_idx, res_len = 0, 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if (j - i + 1) > res_len:
                        res_start_index = i
                        res_len = j - i + 1

        return s[res_start_index : res_start_index + res_len]
