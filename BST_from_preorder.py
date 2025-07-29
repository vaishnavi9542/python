# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        left_el = []
        right_el = []
        for n in preorder:
            if n > preorder[0]:
                right_el.append(n)
            elif n < preorder[0]: 
                left_el.append(n)
        root.left = self.bstFromPreorder(left_el)
        root.right = self.bstFromPreorder(right_el)
        return root
        
