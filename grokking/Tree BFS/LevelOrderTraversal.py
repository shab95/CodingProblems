from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    queue = deque()
    queue.append(root)
    levelSize = 1
    count = 0
    while len(queue) > 0:
        levelSize = len(queue)
        subList = []
        count = 0
        while count < levelSize:
            popped = queue.popleft()
            subList.append(popped.val)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
            count += 1
        result.append(subList)
    return result


'''
Summary:

This problem can be solved by understanding the Breadth First Search algorithm. There are three steps to solving this problem. First,
we need to pop everything currently in the queue. For each element we pop, we need to add their children to the queue. However,
we do not want to end up popping the children too as they will be on the next level. For each element that got popped we add them
to a sublist since they will be on the same level. Once all elements in one level are popped, we can add that sub list to the result.

The tricky part to this problem is getting only one level at a timel. We can do this by getting the size of the queue. The queue's size
will always represent the size of the level. For example, the original queue only has root in it. The length of the queue is one
and the length of the first level is one. We then only pop out items that are within the length of the queue before we start adding
children. This way we don't pop out child elements.

Time Complexity: O(N) - We traverse the tree only once.
Space Complexity: O(N) - The output list requires N space.
'''


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
