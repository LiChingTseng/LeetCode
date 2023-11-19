class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a, b = 1, 1

        total = m+n-2
        k = max(m-1, n-1)
        
        for i in range(k+1, m+n-1):
            a = a*i
        
        for j in range(1, min(m, n)):
            b = b*j

        return a/b
