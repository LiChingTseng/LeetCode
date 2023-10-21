# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

    ## Iteration Solution
        # the goal is to reverse the links between nodes in the linkes list

        prev = None # initialize a pointer to keep track of the previous node
        curr = head # start with the head of the list

        # travel the list until we reach the end
        while curr:
             # store the next node before we change the current node's next
             next_temp = curr.next

             # reverse the current's next pointer to point to the previous one
             curr.next = prev

             # move the prev pointer one step ahead to start the next iteration
             prev = curr

             # move to the next node of the original node
             curr = next_temp
        return prev # return the new head, which is the last node we visited

    # Time Complexity = O(n), assuming that the length of the list is n
    # Space Complexity

    ## Recursive Solution

    # the base case is length of 0 and 1, which is already reversed
    # check for an empty list or a list of length 1
    if (not head) or (not head.next): # head.next=None for the list of length 1 
        return head

    # recursively reverse the rest of the list starting from head.next
    p = self.reverseList(head.next) # p then would be the new head of the reversed list

    # append the current node to the end of the reversed list
    head.next.next = head

    # set the current head to point to None, as it is the new tail  of the reversed list
    head.next = None

    return p







        
