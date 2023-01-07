'''
Problem Statement 
Given a binary tree and a number ‘S’, 
find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
'''


# mycode
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if root == None:
        return False

    if root.val == sum and root.left == None and root.right == None:
        return True

    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


'''
Summary:

This algorithm uses basic DFS in recursive fashion. The trick to solving it is just thinking about it as a tree and understanding
if we come across any leaf node with the sum, then we can return True. However, if we come across a leaf node without the correct sum
and we try to traverse more, then we return false. For me, the difficult part was getting the or statement. This allows any time
that Truth comes up then it will return True. 

The way that the sum is calculated is by actually substracting from the sum. If we were on the correct path and we subtract each
node's value from the sum each time, then by the end we would have the value 0. The second to last value before subtracting and getting
zero would be the value of the last node itself. This is why we can use root.val == sum.

Time Complexity: O(N) - We process each node once.
Space Complexity: O(N) - Space is used to store the recursion stack. Note that this is not a variable.
'''


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
