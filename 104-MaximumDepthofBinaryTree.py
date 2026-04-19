class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return self.maxDepth(root.right)  + 1

        if not root.right:
            return self.maxDepth(root.left)  + 1

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) +  1