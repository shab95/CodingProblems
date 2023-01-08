'''
Problem Statement 
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    # TODO: Write your code here

    return find_current_path(root, sequence, 0)


def find_current_path(currentNode, sequence, sequenceIndex):
    if currentNode == None or sequenceIndex >= len(sequenceIndex):
        return False
    elif currentNode.val == sequence[sequenceIndex] and sequenceIndex == len(sequence) - 1 and currentNode.left == None and currentNode.right == None:
        return True
    elif currentNode.val == sequence[sequenceIndex]:
        return find_current_path(currentNode.left, sequence, sequenceIndex + 1) or find_current_path(currentNode.right, sequence, sequenceIndex + 1)
    else:  # value does not match index
        return False


'''
Summary:

This problem can be solved by using the DFS algorithm. To use DFS, we use a helper function called find_current_path with parameters
of the currentNode, the actual sequence to be found and a sequenceIndex. 

Going through the helper function, the goal is to find a node where the currentNode value is equal to the value of last index in the
list and is a leaf node. Keep in mind we will only be checking for the last index if all the previous indexes have been matched 
properly as well.

If the currentNode does not exist or the sequenceIndex has gone beyond the length of the sequence list, then we can return False.
If the currentNode value matches the sequenceIndex and the sequenceIndex is the last index in the list and the node is a leaf node, then
we can return True. If that does not match but the currentNode value matches the respective element in the sequence denoted by
sequence index, then we can continue iterating down this path. However, if none of those conditions are met that just means
that the currentNode value does not equal the respective element in sequence denoted by the sequence index, so we can return False.

Time Complexity: O(N) - We process each node a maximum of once.
Space Complexity: O(N) - There are no variables that take N space, but the recursive stack can take N space.
'''


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
