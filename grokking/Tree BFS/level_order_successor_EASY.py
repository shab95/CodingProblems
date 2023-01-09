'''
Problem Statement 
Given a binary tree and a node, find the level order successor of the given node in the tree. 
The level order successor is the node that appears right after the given node in the level order traversal.
'''


# mycode
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    # TODO: Write your code here
    if root == None:
        return None

    queue = deque()
    queue.append(root)
    keyFound = False

    while queue:
        popped = queue.popleft()
        if keyFound:
            return popped
        if popped.val == key:
            keyFound = True
        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)
    return None


'''
Summary:

This problem can be solved using BFS. BFS allows us to iterate the tree level by level and it uses a queue. This means it adds elements
to the queue horizontally, which is how it allows us to solve this problem. Once we find the element, we know the next element is
the one we need to return. In this code, we turn on a marker that says the key is found. In the next iteration of the queue, that next
element will be returned

Time Complexity: O(N) - We process each node a maximum once.
Space Complexity: O(N) - The queue structure will a hold a maximum of N/2 space(last level) and it is the last node.
'''


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


main()
