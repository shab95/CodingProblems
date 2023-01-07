'''
Problem Statement 
Find the minimum depth of a binary tree. 
The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
'''

# mycode
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    if root is None:
        return 0

    minCount = 0
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        levelCount = 0
        minCount += 1
        while levelCount < levelSize:
            popped = queue.popleft()
            if popped.left == None and popped.right == None:
                return minCount
            else:
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
            levelCount += 1
    return minCount


'''
Summary:

This algorithm works by using BFS. Essentially, we want to count how many levels there are until we reach our first leaf node. We can do
this by iterating each level and seeing if there is a leaf node. If there is no leaf node, then we can add one to our count because
we are going to have to check one level deeper for the leaf node again.

Once we find the leaf node, we can return the count. However, if there is no leaf node, then we add its children to the queue.

Time Complexity: O(N) - We process every node a maximum of once.
Space Complexity: O(N) - The queue variable can have a max of N nodes(tree is a linked list).

'''


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
