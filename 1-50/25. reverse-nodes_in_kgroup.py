# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        back=ListNode(0)
        back.next=head
        prevgroup=back
        while True:
            kth=self.getkth(prevgroup,k)
            if kth is None:
                break
            nextgroup=kth.next
            prev=nextgroup
            current=prevgroup.next
            while current!=nextgroup:
                temp=current.next
                current.next=prev
                prev=current
                current=temp
            temp=prevgroup.next
            prevgroup.next=kth
            prevgroup=temp
        return back.next
    def getkth(self,current,k):
        while current and k>0:
            current=current.next
            k-=1
        return current
