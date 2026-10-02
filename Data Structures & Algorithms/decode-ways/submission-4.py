class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1                      # 空字符串算一种

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0              # 不能以 0 开头
                continue
            dp[i] = dp[i + 1]          # 选择 1：单独解码 s[i]
            if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                dp[i] += dp[i + 2]     # 选择 2：s[i]s[i+1] 一起解码
        return dp[0]