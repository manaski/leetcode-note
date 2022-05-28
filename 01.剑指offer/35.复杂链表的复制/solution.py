# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.node_map = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head

        if self.node_map[head] is None:
            newNode = Node(head.val)
            newNode.next = self.copyRandomList(head.next)
            newNode.random = self.copyRandomList(head.random)
            self.node_map[head] = newNode
            return newNode
        else:
            return self.node_map[head]

