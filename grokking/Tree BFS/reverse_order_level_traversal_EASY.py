'''
Problem Statement 
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. 
You should populate the values of all nodes in each level from left to right in separate sub-arrays.
'''

# mycode
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()

    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelCount = 0
        level = []
        levelSize = len(queue)
        while levelCount < levelSize:
            popped = queue.popleft()
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
            level.append(popped.val)
            levelCount += 1

        result.appendleft(level)
    return list(result)


'''
Summary:

This algorithm is extremely similar to a normal level order traversal, but the only difference is we initialize result as a deque so
we can append the levels to the left to get the order correct.

The algorithm basically works as a BFS. It traverses by level. The important step is that to add each level once at a time. The trick
to this is basically popping only the things that are currently in the queue. Everything in the queue at the beginning of each iteration
will be on the same level. This is why we do levelCount < levelSize instead of levelCount < len(queue) as the size of the queue
would kepe changing when we append children.

Time Complexity: O(N) - We process each node once.
Space Complexity: O(N) - The output array needs space for each node. The queue variable would also hold a maximum of N/2 nodes at time.
                         It would hold N/2 nodes at the bottom most level.
'''


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
