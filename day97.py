class Solution:
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)

        # Length check
        if m + n != len(s3):
            return False

        # Create DP table
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty strings
        dp[0][0] = True

        # Fill the DP table
        for i in range(m + 1):
            for j in range(n + 1):

                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]

        # Return the final result
        return dp[m][n]