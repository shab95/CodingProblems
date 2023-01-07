'''
Problem Statement 
Given a binary tree where each node can only have a digit (0-9) value, 
each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
'''

# mycode


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    # TODO: Write your code here
    if root == None:
        return 0
    return helper(root, 0)


def helper(root, pathAccumulation):
    pathAccumulation = 10 * pathAccumulation + root.val

    if root.left == None and root.right == None:
        return pathAccumulation

    leftSum, rightSum = 0, 0
    if root.left:
        leftSum = helper(root.left, pathAccumulation)
    if root.right:
        rightSum = helper(root.right, pathAccumulation)
    return leftSum + rightSum


'''
Summary:

This problem can be solved by using DFS. The recursion can be hard to follow, but an example can make it clearer. First, in the main
function, we check if root is None. This is an edge case that we return 0 for. Now, going into the helper, it takes 2 parameters.
One for the current node we are iterating at and one for the current path accumulation. This is the variable we are going to use
to save the path along the way there. 

The first thing we do in helper is multiply the accumulator by 10 and add the current node's value. Because we want the leaf nodes
to be at the one's digit, we need each node above to be multipled by a factor of 10. However, the problem is that we do not know how
many times we need to multiply by 10. This solution multiplies the path accumulation by 10 every time we encounter a new level, so
eventually it will have properly multiplied each node by the 10 the correct number of times. 

Next, we check if the current node is a leaf node. If it is, then we can return the path accumulation number. However, if it is not
a leaf node, then we have to continue iterating down until we find a leaf node. First, we check if a left node exists or right node
exists. Then we just call the function again on the left/right node and the new pathAccumulation. At the end we return the sum of 
the left path and right path. Although it seems like it would only take the initial left and right path of the root, this actually
takes every single path since every child will have a left and right as well.

Time Complexity: O(N) - Every node gets processed once.
Space Complexity: O(N) - The recurstive stack frame will be N long at max(if there's a linked list type tree).
'''


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
