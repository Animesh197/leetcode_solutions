# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def averageOfSubtree(self, root: TreeNode) -> int:
        count =[0]
        def sum_and_count(root):
            if root is None:
                return 0,0
            sum_l,count_l = sum_and_count(root.left)
            sum_r,count_r = sum_and_count(root.right)
            sum_subtree = sum_l + sum_r + root.val
            count_subtree = count_l + count_r + 1

            if (sum_subtree//count_subtree == root.val):
                count[0]+=1
            return sum_subtree,count_subtree #calculated values bhi chahiye
        sum_and_count(root)
        return count[0]

        
        # count=[0]
        # def inorder(root):
        #     if root is None:
        #         return 
        #     inorder(root.left)
        #     ans.append(root.val)
        #     inorder(root.right)

        # def preorder(root):
        #     if root is None:
        #         return None
            
        #     cur_node=root.val
        #     ans=[]
        #     inorder(root)
        #     sum_subtree = sum(ans)
        #     count_subtree = len(ans)
        #     if (cur_node.val == sum_subtree//count_subtree):
        #         count[0]+=1
        #     preorder(root.left)
        #     preorder(root.right)
        # preorder(root)
        # return count[0]


        

        