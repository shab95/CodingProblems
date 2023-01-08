'''
Problem Statement 
Given a binary tree and a number ‘S’, 
find all paths in the tree such that the sum of all the node values of each path equals ‘S’. 
Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
'''

# mycode


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    # TODO: Write your code here
    return helper(root, [], S)


def helper(currNode, currPath, S):
    if currNode == None:
        return 0

    currPath.append(currNode.val)
    countPaths = 0
    runningSum = 0
    for i in range(len(currPath) - 1, -1, -1):
        runningSum += currPath[i]
        if runningSum == S:
            countPaths += 1

    leftPaths = helper(currNode.left, currPath, S)
    rightPaths = helper(currNode.right, currPath, S)
    countPaths += leftPaths + rightPaths

    del currPath[-1]
    return countPaths


'''
Summary:

This algorithm works by using DFS. The algorithm visits every node and checks if adding that node products any paths with the target sum.

The helper function has three variables: the current node, the current path, and the target sum. First, we have to check if the 
current node is None. If it is none, this node is adding 0 paths because it does not change the current path. If it is not none,
then we can add the current node to the path. Now, we have added a new node to the path, we must check if this creates any new subpaths
with the target sum. For this reason, we work the for loop backwards since we only want to see if the new node has produced new paths.
If we used a normal for loop, then we would be considering paths that would have been considered when adding the previous nodes already.
This not only would have caused double counts, but also would not check every possible path. Lastly, we need to continue iterating 
downwards. This is the DFS and recursive portion of the algorithm. Finally, we accumulate all the paths we have found within the for 
loop and the children in the variable called called countpaths, which is being returned at the very end. Before we return countPaths,
we have to delete the current node off the path because it has been fully processed.

Time Complexity: O(N^2) - The recursion processes each node once. For each node, we go through a for loop that can be a maximum of N
                          long. N * N -> N^2
Space Complexity: O(N)  - The recursion stack will hold max N space and the current path will also hold a max N space in the worst
                          case(linked list).
'''


def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    print("Tree has paths: " + str(count_paths(root, 12)))

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
