# class TreeNode:
#     def __init__(self, val, left, right):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def checkTree(self, root: TreeNode) -> bool:
#         if root.val == root.left.val + root.right.val:
#             return True
#         else:
#             return False

# x = TreeNode(10, TreeNode(6), TreeNode(4))

# z = Solution()
# k = z.CheckTree(x)

# print(k)



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkTree(self, root: TreeNode) -> bool:
        return root.val == root.left.val + root.right.val

# create tree
x = TreeNode(10, TreeNode(6), TreeNode(4))

# create solution object and check tree
z = Solution()
k = z.checkTree(x)