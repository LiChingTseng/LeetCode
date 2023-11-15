class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # reach place i by  -> dp[i]
        ## taking 1 step from (i-1) place or 2 steps from (i-2) steps
        
        if n <= 2 : return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
