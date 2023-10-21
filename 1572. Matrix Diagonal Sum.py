class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum = 0
        n = len(mat)
        for i in range(n):
            sum += mat[i][i]

            sum += mat[n-i-1][i]
        
        if n%2 != 0:
            sum -= mat[i//2][i//2]
        
        return sum
