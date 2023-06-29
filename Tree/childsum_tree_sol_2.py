class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def isSumProperty(root):
    # code here
    # solution 2
    if root is None:
        return 1

    queue = [root]
    while len(queue) > 0:
        next_node = queue.pop(0)
        lr_sum = 0
        is_leaf = True
        if next_node.left:
            queue.append(next_node.left)
            lr_sum += next_node.left.data
            is_leaf = False

        if next_node.right:
            queue.append(next_node.right)
            lr_sum += next_node.right.data
            is_leaf = False

        if lr_sum != next_node.data and not is_leaf:
            return 0

    return 1


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(10)
    # root.right = Node(2)
    # root.left.left = Node(4)
    # root.left.right = Node(5)

    print(isSumProperty(root))
