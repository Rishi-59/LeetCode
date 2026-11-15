# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        from collections import deque
        queue = deque()
        result = []
        l_result = []

        if root:
            queue.append(root)
        
        l_node = len(queue)

        while queue:
            while l_node > 0:
                curr = queue.popleft()
                l_result.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
                
                l_node -= 1
            
            l_node = len(queue)
            result.append(l_result)
            l_result = []

        # while queue:
        #     cl_node = 0
        #     while l_node > 0:
        #         curr = queue.popleft()
        #         l_result.append(curr.val)
        #         if curr.left:
        #             cl_node += 1
        #             queue.append(curr.left)
                
        #         if curr.right:
        #             cl_node += 1
        #             queue.append(curr.right)
                
        #         l_node -= 1
            
        #     l_node = cl_node
        #     result.append(l_result)
        #     l_result = []
        

        return result
                