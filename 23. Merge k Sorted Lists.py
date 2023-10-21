# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        # Create a new ListNode representing the head of the merged list.
        # Initialize it with an empty ListNode.
        newList = ListNode()
        # Create a temporary ListNode to build the merged list.
        temporary_list = newList

        # Define a helper function to get the smallest value among the current heads of all lists.
        def getSmallestValue():
            min_value = float('inf')  # Initialize the minimum value as positive infinity.
            min_index = -1  # Initialize the index of the list with the minimum value as -1.
            for i in range(len(lists)):
                # Check if the current list is not empty and its head value is smaller than the current minimum value.
                if lists[i] is not None and lists[i].val < min_value:
                    min_value = lists[i].val
                    min_index = i
            if min_index != -1:
                # If a list with the minimum value is found, move its head to the next element.
                lists[min_index] = lists[min_index].next
            return min_value
        
        # Loop to merge the lists.
        while True:
            x = getSmallestValue()  # Get the smallest value among the current heads of lists.
            if x == float('inf'):
                # If the smallest value is still positive infinity, all lists are empty, so break the loop.
                break
            # Create a new ListNode with the value of the smallest element.
            c = ListNode(val=x)
            # Connect the new node to the merged list.
            temporary_list.next = c
            temporary_list = temporary_list.next  # Move the temporary list pointer forward.
        
        # Return the merged list, excluding the initial empty ListNode.
        return newList.next
