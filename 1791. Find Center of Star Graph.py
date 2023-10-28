class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        
        num = 0

        for i in range(0, 2):
            if edges[0][0] == edges[1][i]:
                num = edges[0][0]
        for i in range(0, 2):
            if edges[0][1] == edges[1][i]:
                num = edges[0][1]
      
        return num
