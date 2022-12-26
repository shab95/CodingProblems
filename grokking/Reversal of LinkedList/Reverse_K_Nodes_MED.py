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


def reverse_every_k_elements(head, k):
    if k < 1 or head is None:
        return head

    previous, current = None, head

    while current is not None:
        lastOfPreviousPart = previous
        lastOfSubList = current

        i = 0
        afterCurrent = None
        while current is not None and i < k:
            afterCurrent = current.next
            current.next = previous
            previous = current
            current = afterCurrent
            i += 1

        if lastOfPreviousPart is not None:
            lastOfPreviousPart.next = previous
        else:
            head = previous

        lastOfSubList.next = current

        previous = lastOfSubList
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next.next.next.next = Node(10)
    head.next.next.next.next.next.next.next.next.next.next = Node(11)

    print("Nodes of original LinkedList are ", end='')
    head.print_list()

    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are ", end='')
    result.print_list()


main()
