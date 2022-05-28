# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchTree(self, root: TreeNode, val: int) -> bool:
        if root == None:
            return True

        if root.val != val:
            return False

        return self.searchTree(root.left, val) and self.searchTree(root.right, val)

    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.searchTree(root.left, root.val) and self.searchTree(root.right, root.val)
