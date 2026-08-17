# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # finding midpoint using floyds fast and slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reversing second half
        second = slow.next
        prev = slow.next = None

        while second != None:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        # merging the two
        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
