# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            mx = float('-inf')

            for _ in range(len(q)):
                node = q.popleft()
                mx = max(mx, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(mx)

        return ans