'''
Problem Statement 
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the same manner for the following levels.
'''


# mycode
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    queue = deque()
    queue.append(root)
    zigZagSwitch = False

    while queue:
        levelCount = 0
        levelSize = len(queue)
        subList = deque()
        while levelCount < levelSize:
            popped = queue.popleft()
            if zigZagSwitch:
                subList.appendleft(popped.val)
            else:
                subList.append(popped.val)

            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)

            levelCount += 1

        result.append(list(subList))
        zigZagSwitch = not zigZagSwitch
    return result


'''
Summary:

This algorithm works by using a switch in conjuction with the level order traversal. The switch allows to change where we add each
element into each sublist. The top level always goes from left to right, the second level goes from right to left, and it keeps 
alternating. We can simply change the left to right and right to left by changing the way we're adding element. If we need to add 
left to right, then we do normal appending. If we need to read right to left, then we append to the beginning of the sublist.

Time Complexity: O(N) - We process each node once.
Space Complexity: O(N) - The output result needs N space and the queue variable uses a max of N/2 space.
'''


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
