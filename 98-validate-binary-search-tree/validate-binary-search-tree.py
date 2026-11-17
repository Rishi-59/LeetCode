# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # res = True
        # def validate(node, l, u):
        #     nonlocal res
        #     if l >= node.val or node.val >= u:
        #         res = False
        #         return
        #     if node.left:
        #         validate(node.left, l, node.val)
        #     if node.right:
        #         validate(node.right, node.val, u)
        #     return

        # validate(root, float('-inf'), float('inf')) 
        # return res    
    

        def validate(node, lower, upper):
            if node is None:
                return True

            if not lower < node.val < upper:
                return False

            return (
                validate(node.left, lower, node.val)
                and
                validate(node.right, node.val, upper)
            )

        return validate(root, float('-inf'), float('inf'))