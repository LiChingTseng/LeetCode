# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: boo
        """

        if not head or not head.next:
            print('1')
            return False

        ## Fast and Slow Technique
        #   if the fast and slow pointers meet at the same node then there is a loop
        fast = slow = head

        while fast!=None and fast.next != None:
            print('2')
            fast = fast.next.next
            slow = slow.next

            if (slow == fast):
                return True
        
        print('3')
        # if the traversal reaches to NULL
        return False
        
