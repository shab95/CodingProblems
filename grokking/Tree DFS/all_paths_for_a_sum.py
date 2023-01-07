'''
Problem Statement 
Given a binary tree and a number ‘S’, 
find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
'''


# mycode
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    # TODO: Write your code here
    helper(root, sum, [], allPaths)
    return allPaths


def helper(root, sum, currentPath, allPaths):
    if root == None:
        return

    currentPath.append(root.val)

    if root.val == sum and root.left == None and root.right == None:
        permCurrentPath = list(currentPath)
        allPaths.append(permCurrentPath)
    else:
        helper(root.left, sum - root.val, currentPath, allPaths)
        helper(root.right, sum - root.val, currentPath, allPaths)
    del currentPath[-1]


'''
Summary:

This algorithm can be solved using the DFS technique. Because DFS is mainly done with recursion and we do not have enough parameters, we
make a helper function. 

This helper function has a current path variable that keeps track of the path we have gone through so far. We also keep
an allPaths variable that keeps track of all the valid paths. 

Now, I'll be describing how the helper function works. The helper function first starts at root. The program goes through each 
path in a DFS manner in that it goes all the way done each time and then only comes back up afterwards. The first line is a check to 
see if we have gone deeper and beyond a leaf node. If have gone beyond a leaf node, then that means that leaf node is not valid
as it would have stopped at the next check we'll discuss if it was valid. In this case, we can just stop the function from continuing
because there are no more children to continue iterating through.

The next check is to see if we stopped at a leaf node where the path does add up to the sum. Remember we get the sum by not keeping a
constant running sum but subtracting from the sum throughout the path. Subtract all the values in the correct path from the target sum
given will result in the target sum being zero at the end. If we are on the corernt path, then that means before we subtract the last 
node's value from the sum the subtracted running sum will equal that last leaf node's value. This is because we know if it is the correct
path, then subtracting that value will make the subtracted running sum zero. This is why we do node.val == sum and we ensure it is 
a full path by checking it is a leaf node.

In the case, the path is correct. We want to save the current path to all paths. This is why we append currentPath to allPaths.
We also save the currentPath as a list because this will create a copy. Otherwise we will lose the pointers to the saved correct paths
once the helper function ends. 

If the program did not stop at the previous checks that means the node is either a leaf node with an incorrect path or a higher node.
To continue traversing down the list, we recursively call the program on both the left and right children and update the subtracted
running sum. 

Finally, we delete the last element in the current Path variable. Why? Because we are in DFS and complete processing the element, we need
to go backwards to continue evaluating further elements. 

Time Complexity: O(N) - We process each node once.
Space Complexity: O(N) - We store a maximum of all nodes in the currentPath variable(if it's a linkedlist).
'''


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
