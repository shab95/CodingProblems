'''
Problem Statement 
Given a binary tree, populate an array to represent the averages of all of its levels.
'''

# mycode
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if root == None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        levelCount = 0
        levelSum = 0
        while levelCount < levelSize:
            popped = queue.popleft()
            levelSum += popped.val
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
            levelCount += 1
        avg = levelSum/levelCount
        result.append(avg)
    return result


'''
Summary:

This problem can be solved by level traversing with a BFS. We use the technique of only iterating one queue at a time. This can be done
by only going through the queue's length before any children is added on. If you think about it the queue before every iteration of
the inner while loop will contain the nodes to one level. Finally, you can take the average by summing the values of each level
and dividing it by the size of the level(length of queue before appending children).

Time Complexity: O(N) - We process every node once.
Space Complexity: O(N) - Queue uses max N/2 elements at one time.
'''


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
