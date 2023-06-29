def mirror(self, root):
    # Code here
    # queue = [root]
    # while (len(queue) > 0):
    #     next_node = queue.pop(0)

    if root.left or root.right:
        root.left, root.right = root.right, root.left