# {
# Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(50000)
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input 
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


# } Driver Code Ends
# User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:
    def Ancestors(self, root, target):
        '''
        :param root: root of the given tree.
        :return: None, print the space separated post ancestors of given target., don't print new line
        '''
        # code here
        queue = []
        queue.append(root)

        i = 0
        while (i < len(queue)):
            next_node = queue[i]
            if next_node.data == target:
                break

            if next_node.left:
                queue.append(next_node.left)
                if next_node.left.data == target:
                    break

            if next_node.right:
                queue.append(next_node.right)
                if next_node.right.data == target:
                    break
            i += 1

        ancestors = []
        for i in range(len(queue) - 1, -1, -1):
            node = queue[i]
            # if target == root.data:
            #     break

            if node.right and node.right.data == target:
                target = node.data
                ancestors.append(node.data)

            if node.left and node.left.data == target:
                target = node.data
                ancestors.append(node.data)


        print(ancestors)

    # {


# Driver Code Starts.
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(7)
    root.left.right = Node(5)

    Solution().Ancestors(root, 7)

# } Driver Code Ends