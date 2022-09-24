def helper(self, node, curSum, curPath):
        #print(curPath)
        if not node:
            return 
        
        if curSum == node.val and not node.left and not node.right:
            curPath.append(node.val)
            print(curPath)
            self.res.append(curPath.copy())
            return
        
        
        curPath.append(node.val)
        self.helper(node.left,curSum - node.val ,curPath)
        self.helper(node.right,curSum - node.val ,curPath)
        curPath.pop()
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.helper(root, targetSum, [])
        return self.res
