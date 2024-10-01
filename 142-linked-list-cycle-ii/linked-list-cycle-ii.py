# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast: # if the pointers meet, theres a cycle
                slow = head # reset the slow pointer to the head of the linkedlist
                while slow != fast:  #to find the start point of the linkedlist until they meet
                    slow = slow.next # move them at the same speed
                    fast = fast.next
                return slow #find the start of the loop
        return None

            