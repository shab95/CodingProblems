class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


'''
Summary:

This problem can be solved using the fast slow pointers technique. The fast pointer always moves two steps in one iteration and the slow
pointer moves one step in one iteration. That means the fast pointer will always be double the distance the slow pointer has went.
As a result, it also means that the slow pointer has covered half the distance the fast pointer has. If the fast pointer has traveled
the entiriety of the linkedlist, then that means the slow pointer is half way through the list and will be pointing at the middle node.

Time Complexity: O(N) - The fast pointer went across the whole list, processing every other element. The slow pointer only covered
                        half the linkedlist. N/2 + N/2 -> N
Space Complexity: O(1) - No extra space is needed.
'''


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()
