class Solution:
    # Function to check whether all nodes of a tree have the value
    # equal to the sum of their child nodes.
    def isSumProperty(self, root):

        # if node is null or both child nodes are null, we return true.
        if root is None:
            return 1
        if root.left is None and root.right is None:
            return 1

        val_root = root.data
        val_left, val_right = 0, 0

        # if left child is not null then we store its value.
        if root.left is not None:
            val_left = root.left.data

        # if right child is not null then we store its value.
        if root.right is not None:
            val_right = root.right.data

        # if sum of stored data of left and right child is equal to the current
        # node data and recursively for the left and right subtree, parent data
        # is equal to sum of child data then we return true else false.
        if val_root != val_left + val_right:
            return 0
        return (self.isSumProperty(root.left) & self.isSumProperty(root.right))