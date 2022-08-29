
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def travel(p, level):
          if not p:
            return level
          
          l1 = travel(p.left, level + 1)
          l2 = travel(p.right, level + 1)
        
          level = max(l1, l2)
          return level
        
        return travel(root, 0)