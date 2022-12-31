class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


def has_cycle(head):
    slow, fast = head, head

    while (fast and fast.next):
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


'''
Summary:

This problem requires the application of the fast, slow pointer technique. Here is our two scenarios. 

If the linkedlist has no cycle. Then the fast pointer wil reach the end of the list within the N/2 steps. 

If the linkedlist has a cycle. Then the fast pointer and slow pointer will go in circles. However, there is a guarantee that the slow 
and fast pointer eventually meet. We can boil this down to two circumstances. If the slow pointer is ever exactly one step ahead of
the fast pointer. Then on the next iteration they will meet. If the slow pointer is ever exactly two steps ahead of the fast pointer,
then on the next iteration the slow pointer will be only one step ahead on the next iteration. This brings us back to scenario 1 where
the slow pointer is only one step ahead of the fast pointer and they will meet on the next iteration.

This code works by continuing to increase a fast pointer by 2 steps and a slow pointer by 1 step. As long as the fast pointer
and the fast pointer's next node is not None/Null/Nil, then we can continue checking if the fast and slow pointer are equal.
If the fast pointer or fast's next pointer is None/Null/Nil, then that means there is no cycle and the linked list has ended.

Time Complexity: O(N) - If there is no cycle, then it will take N/2 iterations for the fast pointer to find None. If there is a cycle, 
                        then the fast pointer and slow pointer will meet after k cycles. 
Space Complexity: O(1) - No extra space is used.
'''


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))


main()
