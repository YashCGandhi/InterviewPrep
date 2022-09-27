def flatten(self, root: Optional[TreeNode]) -> None:
        node = root
        
        def flat(node):
            if not node:
                return
            
            flat(node.left)
            flat(node.right)
            if node.left:
                tmp = node.right
                node.right = node.left
                node.left = None
                
                # get to the right most node and then connect it to the tmp
                while node.right:
                    node = node.right
                node.right = tmp
            
        flat(node)
        return root
