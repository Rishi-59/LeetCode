# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root

        return left if left else right
        # path = []

        # def path_finder(curr, target):
        #     if curr is None:
        #         return False

        #     path.append(curr)

        #     if curr == target:
        #         return True

        #     if path_finder(curr.left, target) or path_finder(curr.right, target):
        #         return True

        #     path.pop()
        #     return False

        # path_finder(root, p)
        # p_path = path.copy()
        # path = []
        # path_finder(root, q)
        # q_path = path.copy()

        # lca = root
        # for i in range(min(len(p_path), len(q_path))):
        #     if p_path[i] == q_path[i]:
        #         lca = p_path[i]
        #     else:
        #         break

        # return lca
