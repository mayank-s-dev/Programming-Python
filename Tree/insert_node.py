# Python program to insert element in binary tree
class newNode:

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


""" Inorder traversal of a binary tree"""


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.key, end=" ")
    inorder(root.right)


def create_and_add(node, key, isLeft):
    new = newNode(12)
    if isLeft:
        node.left = new
    else:
        node.right = new


def insert_level_order(root, key):
    if root is None:
        root = newNode(12)
        return

    queue = [root]
    while len(queue) > 0:
        next_node = queue.pop(0)

        if next_node.left:
            queue.append(next_node.left)
        else:
            create_and_add(next_node, key, True)
            break

        if next_node.right:
            queue.append(next_node.right)
        else:
            create_and_add(next_node, key, False)
            break



# Driver code
if __name__ == '__main__':
    # root = newNode(10)
    # root.left = newNode(11)
    # root.left.left = newNode(7)
    # root.right = newNode(9)
    # root.right.left = newNode(15)
    # root.right.right = newNode(8)
    #
    # print("Inorder traversal before insertion:", end=" ")
    # inorder(root)

    key = 12
    root = None
    insert_level_order(root, key)

    print("Inorder traversal after insertion:", end=" ")
    inorder(root)
