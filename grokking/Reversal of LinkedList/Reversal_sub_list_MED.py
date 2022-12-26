from multiprocessing import current_process


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


def reverse_sub_list(head, p, q):
    counter = 1
    start = head
    prev = None
    while start is not None and counter < p:
        prev = start
        start = start.next
        counter += 1

    lastNodeOfFirstPart = prev

    lastNodeOfSubList = start
    afterStart = next

    while start is not None and counter < q + 1:
        afterStart = start.next
        start.next = prev
        prev = start
        start = afterStart
        counter += 1

    if lastNodeOfFirstPart is not None:
        lastNodeOfFirstPart.next = prev
    else:
        head = prev

    lastNodeOfSubList.next = start

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are ", end='')
    # head.print_list()

    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are ", end='')
    # result.print_list()


main()
