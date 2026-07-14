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
        # -----------Extra Memory
        # stack = []
        # curr = head
        # while curr:
        #     stack.append(curr.val)
        #     curr = curr.next

        # curr = head
        # for i in range(len(stack)-1,-1,-1):
        #     curr.val = stack.pop()
        #     curr = curr.next
        
        # return head

        # -----------Iterative
        # prev = None
        # temp = head

        # while temp:
        #     front = temp.next
        #     temp.next = prev
        #     prev = temp
        #     temp = front

        # head = prev
        # return head

        # -----------Recursion
        def reverse(head):
            if not head or head.next == None:
                return head
            newHead = reverse(head.next)
            front = head.next
            front.next = head
            head.next = None
            return newHead

        return reverse(head)
        