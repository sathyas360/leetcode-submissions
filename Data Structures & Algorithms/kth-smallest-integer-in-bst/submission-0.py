# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root, output):
        if root:
            self.inorderTraversal(root.left, output)
            output.append(root.val)
            self.inorderTraversal(root.right, output)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        self.inorderTraversal(root, output)
        return output[k-1]