'''
Problem Statement 
Given a binary tree, connect each node with its level order successor. 
The last node of each level should point to a null node.
'''


# mycode
from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connect_level_order_siblings(root):
    # TODO: Write your code here
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        levelCount = 0
        while levelCount < levelSize:
            popped = queue.popleft()
            if levelCount + 1 == levelSize:
                popped.next = None
            else:
                popped.next = queue[0]
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
            levelCount += 1
    return


'''
Summary:

This problem can be solved with BFS since we need to traverse the tree by level.

To connect the nodes to each other we need to traverse each level from left to right. This is why we append the left child before the
right child. To connect the actual nodes, we take the current popped node and treat that as our current node. If we are not at the end
of our level(which we check by seeing if levelCount + 1 == levelSize), then we can get the next node by doing queue[0]. However, if
this is the last node of the level, then that conditional will become True and we can point the current node to None.

Time Complexity: O(N) - We process each node once.
Space Complexity: O(N) - The queue variable will store a maximum of N/2.
'''


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
