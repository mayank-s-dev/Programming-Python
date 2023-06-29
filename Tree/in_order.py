class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


class Solution:
    a = [1, 2]
    def add(self, root_node, res):
        # code here
        if root_node == None:
            return

        self.InOrder(root_node.left, res)
        res.append(root_node.data)
        self.InOrder(root_node.right, res)

    def InOrder(self, root_node, res=[]):
        res = []
        self.add(root_node, res)
        return res


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # Function call
    s=Solution().InOrder(root)
    print(s)