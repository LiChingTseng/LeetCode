# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        """
        Step 1. Find the Middle node (2 pointer: slow and fast pointerd technique)
        Step2. Reverse the second half
        Step 3. Merge the two halves (2 pointer)
        """

        if not head:
            return

        # Step 1. find the middle of the linked list (Problem 876: Middle of the linked list)
        # Slow and Fast Technique
        #   'fast' moves 2 steps at a time, while 'slow' moves 1 step a time
        #   when 'fast' reach the end of the list, 'slow' reach the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2. Reverse the second half of the linked list (Problem 206. Reverse the Linked List)
        prev = None
        curr = slow
        while curr: 
            curr.next, prev, curr = prev, curr, curr.next
        
        # Step 3. Merge the two halves linked list (Problem 21. Merged two linked list)
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        
         




        


