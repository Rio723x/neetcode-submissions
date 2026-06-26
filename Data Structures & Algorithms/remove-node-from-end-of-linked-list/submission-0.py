# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length+=1
        if length == n:
            return head.next
        temp1 = head
        for i in range ( length - n - 1):
            temp1 = temp1.next
        temp1.next = temp1.next.next 

        return head
        