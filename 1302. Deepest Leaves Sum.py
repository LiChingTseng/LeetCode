# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        next_level = deque([root,])

        while next_level:

            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            for node in curr_level:

                # add children from next level to buid up the updated queue
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
        return sum([node.val for node in curr_level])
