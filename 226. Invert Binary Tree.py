class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def invertTree(self, root):
    p = root
    while p:
      self.invertTree(p.left)
      self.invertTree(p.right)

    p.left, p.right = p.right, p.left

root = [2,1,3]

s = Solution()
print(s.invertTree(root))