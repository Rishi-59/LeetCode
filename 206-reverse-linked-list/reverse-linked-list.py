# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head
        for i in range(len(stack)-1,-1,-1):
            curr.val = stack.pop()
            curr = curr.next
        
        return head