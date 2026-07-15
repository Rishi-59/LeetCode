# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-101)
        curr = head
        while curr:
            if dummy.val != curr.val:
                dummy.next = curr
                dummy = dummy.next
            else:
                curr = curr.next
        dummy.next = None
        return head
        