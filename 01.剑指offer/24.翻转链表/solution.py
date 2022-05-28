class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        hnode = ListNode()

        while head != None:
            next = head.next
            head.next = hnode.next
            hnode.next = head
            head = next

        return hnode.next
