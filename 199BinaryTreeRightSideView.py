s Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        output = []
        
        q = [root, ]
        
        while q:
            size = len(q)
            
            while size > 0:
                
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size-=1
                
            output.append(node.val)
        return output
            
