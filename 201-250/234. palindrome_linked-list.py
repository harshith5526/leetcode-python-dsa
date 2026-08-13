# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None and head.next is None:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        first=head
        second=self.reverse(slow)
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True
    def reverse(self,head):
        prev=None
        curr=head
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        return prev
