# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        firstNode = ListNode(0)
        beforeNode = firstNode
        
        while 1:
            if l1 and l2:
                if l1.val <= l2.val:
                    beforeNode.next = l1
                    beforeNode = l1
                    l1 = l1.next

                else:
                    beforeNode.next = l2
                    beforeNode = l2
                    l2 = l2.next

            elif l1:
                beforeNode.next = l1
                break

            elif l2:
                beforeNode.next = l2
                break

            else:
                break

        return firstNode.next
