class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points=sorted(points,key=lambda x:x[1])
        c=0
        end=float('-inf')
        for i in points:
            if i[0]>end:
                c+=1
                end=i[1]
        return c
        
