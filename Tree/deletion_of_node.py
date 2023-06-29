class newNode:

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def delete_deepest(root, delete_node):
    queue = [root]
    while len(queue) > 0:
        next_node = queue.pop(0)
        if root is delete_node:
            root = None
            return

        if next_node.left:
            if next_node.left == delete_node:
                next_node.left = None
                return
            queue.append(next_node.left)

        if next_node.right:
            if next_node.right == delete_node:
                next_node.right = None
                return
            queue.append(next_node.right)


def find_deepest(root, key):
    if root is None:
        return None

    if root.left is None and root.right is None:
        if root.key == key:
            return None
        else:
            return root

    queue = [root]
    key_node = None
    while len(queue) > 0:
        next_node = queue.pop(0)
        if next_node.key == key:
            key_node = next_node

        if next_node.left:
            queue.append(next_node.left)

        if next_node.right:
            queue.append(next_node.right)

    if key_node is not None:
        delete_deepest(root, next_node)
        key_node.key = next_node.key


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.key, end=" ")
    inorder(root.right)


# Driver code
if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(12)
    root.right.left = newNode(15)
    root.right.right = newNode(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    key = 12
    find_deepest(root, key)

    print("Inorder traversal after insertion:", end=" ")
    inorder(root)
