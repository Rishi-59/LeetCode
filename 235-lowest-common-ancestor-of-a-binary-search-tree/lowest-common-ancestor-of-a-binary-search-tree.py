# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root
        while lca.val < p.val and lca.val < q.val or lca.val > p.val and lca.val > q.val:
            if lca.val < p.val and lca.val < q.val:
                lca = lca.right
            else:
                lca = lca.left
        return lca