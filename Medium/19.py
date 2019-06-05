class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        NodeList = []
        nowNode = head
        while True:
            NodeList.append(nowNode)
            if nowNode.next is None:
                break
            else:
                nowNode = nowNode.next
        if len(ListNode) == 1:
            return None

        if n == 1:
            NodeList[len(NodeList)-n-1].next = None
        elif n == len(NodeList):
            return NodeList[1]
        else:
            NodeList[len(NodeList)-n-1].next = NodeList[len(NodeList)-n+1]
        return NodeList[0]

def main():
    sol = Solution()

if __name__ == "__main__":
    main()
