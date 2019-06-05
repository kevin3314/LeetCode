# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_node = ListNode(0)
        dummy_node.next = head
        before_node = dummy_node
        head_node = head

        while 1:
            # if last of list, then break!
            if head_node is None or head_node.next is None:
                break

            # next node exist.
            next_node = head_node.next.next
            head_node.next.next = head_node
            before_node.next = head_node.next
            before_node = head_node
            head_node.next = next_node
            head_node = next_node

        return dummy_node.next
