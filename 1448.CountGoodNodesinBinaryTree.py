class Solution:
    def __init__(self):
        self.cnt = 0
    def goodNodes(self, root: TreeNode) -> int:
        def recur(node, curMax):
            if not node:
                return
            if node.val >= curMax:
                curMax = node.val
                self.cnt += 1
            
            recur(node.left, curMax)
            recur(node.right, curMax)

        recur(root, float("-inf"))
        return self.cnt
