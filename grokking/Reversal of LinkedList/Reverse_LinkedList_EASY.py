class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

# Explanation:
# The previous pointer is initially at Null and the current pointer is at the head. We also have a pointer after the current.
# The order of operations: the pointer which goes after current is set to the node right after current so it is saved for later.
# The curr node now reverses and points at the previous node. Previous can now set to be the current node, since the reversal is done.
# Finally, we used the node after current we saved from before and set it to the curr variable so we can continue reversing
# the rest of the list.


def reverse(head):
    prev = None
    curr = head
    while (curr):
        afterCurr = curr.next
        curr.next = prev
        prev = curr
        curr = afterCurr
    head = prev
    return head


'''
Summary:

This problem can be done by iterating the list once and keeping three pointers. One for the node we are currently looking at, curr.
One for the node before the one we are looking at, prev. Lastly, there is a pointer for the one after the one we're looking at, afterCurr.

We start at the head node and save the head.next to afterCurr for storage. We then point curr to prev. This is what actually reverses
the linked list. Now, to iterate forward we move prev and curr up one step. We do this by setting prev to curr and curr to 
the afterCurr variable we stored before. We keep doing this until curr becomes null/none. Null/none indicates the end of the linked list.

Since curr is null and prev is set to the node right before curr, we know that prev is the node that is the end of the original linkedlist.
This also means that it is the first node in the reversed linked list, which is why we set head to prev and return head.

Time Complexity: O(N) - One iteration is all that is needed.
Space Complexity: O(1) - No extra space is used.
'''


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are ", end='')
    head.print_list()

    result = reverse(head)
    print("Nodes of reversed LinkedList are ", end='')
    result.print_list()


main()
