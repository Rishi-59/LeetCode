# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l3 = ListNode()
        # head = l3
        # carry = 0
        # while l1 and l2:
        #     add = l1.val + l2.val + carry
        #     if add > 9 :
        #         carry = add // 10
        #         add = add % 10
        #     else :
        #         carry = 0
        #     l3.val = add
        #     l1 = l1.next
        #     l2 = l2.next
        #     if l1 or l2 or carry:
        #         l3.next = ListNode()
        #         l3 = l3.next 

        # while l1:
        #     add = l1.val + carry
        #     if add > 9 :
        #         carry = add // 10
        #         add = add % 10
        #     else :
        #         carry = 0
        #     l3.val = add
        #     l1 = l1.next
        #     if l1 or carry:
        #         l3.next = ListNode()
        #         l3 = l3.next 
        
        # while l2:
        #     add = l2.val + carry
        #     if add > 9 :
        #         carry = add // 10
        #         add = add % 10
        #     else :
        #         carry = 0
        #     l3.val = add
        #     l2 = l2.next
        #     if l2 or carry:
        #         l3.next = ListNode()
        #         l3 = l3.next 
        
        # if carry:
        #     l3.val = carry

        carry = 0
        newList = ListNode()
        curr = newList

        while carry or l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            newNode = ListNode(total%10)
            carry = total // 10

            curr.next = newNode
            curr = newNode

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return newList.next