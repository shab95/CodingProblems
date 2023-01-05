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
    # check if p is q edge case
    if p == q:
        return head

    # skipping p - 1 nodes
    count = 1
    nodeBeforeP = None  # saving to connect later to the reversed linkedlist
    pNode = head
    while count < p:
        nodeBeforeP = curr
        pNode = pNode.next
        count += 1

    curr = pNode
    prev = None
    while (curr and curr.value <= q):  # reversing until we have pointed q node to q - 1 node
        afterCurr = curr.next
        curr.next = prev
        prev = curr
        curr = afterCurr

    qNode = prev  # qNode is prev. changed variables for it to make sense
    if nodeBeforeP:
        nodeBeforeP.next = qNode  # connecting the node before p that we saved to q node
    else:
        head = qNode

    # connecting the p node that's now at the other end to the other side of the linkedlist
    pNode.next = curr
    return head


'''
Summary:

This problem can be solved by first splitting it into 3 different parts. The first part is getting to the pth node. The second part is
reversing the specific group of nodes. The last part is connecting the seperate parts of the linkedlist back together. Now, let's split
the linkedlist into multiple parts. The first part of the linked list is the part before of the group of nodes that need to be
reversed. The second part of the linked list is the group of nodes that need to be reversed. The last part of the linked list is the
part after the group of nodes that need to be reversed.

First, we need to iterate to the pth node. We can do this by keeping a counter and increasing the current node until the counter
reaches the pth node. We also set a variable to the node before p for connecting purposes later. We also save the pth node for the same
reason.

Now, we can concentrate on reversing the part that needs to be reversed. We set a while loop for the current value to exceed the qth
node. We also ensure that the current node is not null and we have reached the end of the list on each iteration. To actually reverse
this group, we use three pointers. A previous pointer, current pointer, and then an afterCurrent pointer. First, the afterCurrent pointer
saves the node after current for iterating purposes. Then we reverse the list by setting the next of the current pointer to
the previous pointer. Then we iterate by setting previous to current and current to the afterCurrent variable we saved earlier.

Now, we are at the last part where we connect all the parts of the linkedlist back together. If everything was done properly, the current
pointer points to the node after q and previous will be the qth node. If the node before P we saved earlier was not Null, then we
can set the next of this node to the qth node(prev). This connects the first part of the linked list to the reversed group. To connect
the reversed group to the last part of the linked list, we take the pth node that we saved earlier and save it's next attribute
to the pointer called current. We do this because the pth node is now properly reversed and at the end of the reversed group. The
current pointer is also at the first node after the reversed group as mentioned earlier. 

Now, we can simply return head, which should be the beginning of the list and was not altered.

The edge case of p equaling q was addressed at the very beginning and in this case, we simply returned head.

Time Complexity: O(N) - Only one iteration was needed.
Space Complexity: O(1) - No extra spaced was needed.
'''


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are ", end='')
    head.print_list()

    result = reverse_sub_list(head, 2, 5)
    print("Nodes of reversed LinkedList are ", end='')
    result.print_list()


main()
