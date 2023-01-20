# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        # Preorder to create a string
        def recur_serialize(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = recur_serialize(root.left, string)
                string = recur_serialize(root.right, string)
            return string
        return recur_serialize(root, "")        

    def deserialize(self, data):
        # Preorder traversal to deserialize it
        def recur_deserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            
            root = TreeNode(l.pop(0))
            root.left = recur_deserialize(l)
            root.right = recur_deserialize(l)
            return root
        
        data_list = data.split(",")
        root = recur_deserialize(data_list)
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
