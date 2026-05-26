# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0;

        def recurse(root: Optional[TreeNode], depth: int) -> int:
            if root is None:
                return 0
            else:
                depth += 1
                left = recurse(root.left, depth)
                right = recurse(root.right, depth)
                if left > right:
                    return left + 1
                else:
                    return right + 1

        depth = recurse(root, 0)

        return depth

            