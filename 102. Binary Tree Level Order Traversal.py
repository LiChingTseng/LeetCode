# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        output = []

        def traverseLevel(root, levelIndex):
            if len(output) < levelIndex + 1:
                output.append([root.val])
            else:
                output[levelIndex].append(root.val)

            if root.left:
                traverseLevel(root.left, levelIndex + 1)
            if root.right:
                traverseLevel(root.right, levelIndex + 1)

        traverseLevel(root, 0)
        return output




