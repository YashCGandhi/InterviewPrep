def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if not root:
            return []
        
        queue = [root, ]
        
        while queue:
            
            # size is used to make sure that only the elements of the current level are being used
            size = len(queue)
            
            while size > 0:
                node = queue.pop(0)
                
                # add the left and right of node into the queue for next iteration
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    
                size -= 1
            # when the size becomes 0 the element will be the right most element in that level so append it to the output
            output.append(node.val)
        return output
        
