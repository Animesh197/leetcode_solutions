# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root):
        answer = 0

        def dfs(node):
            nonlocal answer

            if node is None:
                return -1, -1

            left = dfs(node.left)
            right = dfs(node.right)

            left_path = left[1] + 1
            right_path = right[0] + 1

            answer = max(answer, left_path, right_path)

            return left_path, right_path

        dfs(root)

        return answer
        