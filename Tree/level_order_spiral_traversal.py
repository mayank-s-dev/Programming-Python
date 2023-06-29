"""using deque: solution 3

"""

"""using stack : solution 2
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_spiral(root):
    s1 = [] # left to right
    s2 = [] # right to left

    s1.append(root)
    res = []
    while len(s1) > 0 or len(s2) > 0:
        while len(s1) > 0:
            next_node = s1[-1]  # to fetch the top most element from stack
            s1.pop()
            if next_node is None:
                return

            res.append(next_node.data)

            if next_node.right:
                s2.append(next_node.right)
            if next_node.left:
                s2.append(next_node.left)

        while len(s2) > 0:
            next_node = s2[-1]  # to fetch the top most element from stack
            s2.pop()
            if next_node is None:
                return

            res.append(next_node.data)

            if next_node.left:
                s1.append(next_node.left)
            if next_node.right:
                s1.append(next_node.right)

    return res






# Driver Code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    print("Spiral Order traversal of",
          "binary tree is ")
    res = print_spiral(root)
    print(res)


"""

"""
# Recursive Python program for level
# order traversal of Binary Tree


# A node structure
class newNode:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    ltr = False
    for i in range(1, h + 1):
        printCurrentLevel(root, i, ltr)
        ltr = not ltr


# Print nodes at a current level
def printCurrentLevel(root, level, ltr):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        if ltr:
            printCurrentLevel(root.left, level - 1, ltr)
            printCurrentLevel(root.right, level - 1, ltr)
        else:
            printCurrentLevel(root.right, level - 1, ltr)
            printCurrentLevel(root.left, level - 1, ltr)


# Compute the height of a tree--the number of nodes
# along the longest path from the root node down to
# the farthest leaf node
def height(node):
    if node is None:
        return 0
    else:

        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


# Driver program to test above function
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(7)
    root.left.right = newNode(6)
    root.right.left = newNode(5)
    root.right.right = newNode(4)

    print("Level order traversal of binary tree is -")
    printLevelOrder(root)
"""
