class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        item can increase height of min(maximum of that row, maximum of that column)
        ⇒ Step 1. iterations to find out each maximum of each row and column
        ⇒ Step 2. Update all the increase in skyline
        """
        
        # get the maximum value in each row and column
        # zip(*grid) transpose the grid
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        ans = sum(min(row_maxes[r], col_maxes[c]) - val

                    # r: index of rows, row: each row
                    for r, row in enumerate(grid) 

                    # inside the first loop, iterate index of column and the value of elements
                    for c, val in enumerate(row)) 
        
        return ans
         
