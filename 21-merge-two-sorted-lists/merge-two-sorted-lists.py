# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
                
        t1 = list1
        t2 = list2
        dNode = ListNode(-1)
        temp = dNode

        while t1 and t2:
            if t1.val <= t2.val:
                temp.next = t1
                temp = temp.next
                t1 = t1.next
            else:
                temp.next = t2
                temp = temp.next
                t2 = t2.next

        if t1:
            temp.next = t1
        if t2:
            temp.next = t2
            
        return dNode.next

