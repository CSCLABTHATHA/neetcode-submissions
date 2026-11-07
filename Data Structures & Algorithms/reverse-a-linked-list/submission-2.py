# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev

'''
class Solution:
    def reverseList(self,head):
        def swapper(curr,prev=None):
            if not curr:
                return prev
            nex = curr.next
            curr.next = prev
            return swapper(nex,curr)
        
        return swapper(head)