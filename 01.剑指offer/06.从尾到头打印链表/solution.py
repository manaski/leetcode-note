
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = list()

        while head != None:
            res.insert(0, head.val)
            head = head.next

        return res

