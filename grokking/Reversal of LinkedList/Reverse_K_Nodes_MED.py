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
    if k < 2 or head == None:
        return head

    prev = None
    curr = head
    while curr:
        beforeSubList = prev
        firstOfOGSubList = curr
        counter = 0
        while curr and counter < k:
            afterCurr = curr.next
            curr.next = prev
            prev = curr
            curr = afterCurr
            counter += 1

        lastOfOGSubList = prev
        afterSubList = curr
        if beforeSubList == None:
            head = lastOfOGSubList
        else:
            beforeSubList.next = lastOfOGSubList
        firstOfOGSubList.next = afterSubList

        prev = firstOfOGSubList
    return head


'''
Summary:

This problem can be solved very similarly to the reversal sub list problem. This algorithm can be best described by using an example
and going through the code. Here is an attempt to describe it.

First, we do a simple check. If k < 2, then that means we are not actually reversing any nodes and everything will stay the same. Second,
we set our variables to do our swaps. We always need three variables to swap. In this case, we use a previous, which will be Null at 
first and we use a current pointer. Current will point to the head at first. 

Now, our while loop will only end once we have iterated through the entire list, which is why we are checking if current is equal to 
Null. Inside the while loop, we have to start saving variables so we can wire the linkedlist correctly after we reverse a group 
of nodes. That is the reason we save the node before the sublist. We also save the node that is originally at the beginning of the
sublist, but will eventually be at the end of the sublist once reversed. 

Next, we need to reverse the sublist. We can do this by saving the pointer after current(afterCurr). Then actually reversing by changing
the next of the curr pointer to previous. Then we can iterate to the next node of the sublist by changing the previous to current
and current to the afterCurr pointer we saved earlier. We do this until we eventually reverse K nodes or we reach Null.

Finally, we have to rewire the linkedlist to connect it back together. First, we will connect the end of the previous sublist
to the start of the new reversed sub list. To understand how to do this, we must understand where our curr and prev pointers are.
Curr is pointing to the node to the right of the end of the sublist we just reversed. This can also be called the beginning of the
sublist we have to reverse next. Prev is pointing to the end of the sublist we just reversed. This can also be called the beginning
of the reversed sublist. To connect the end of the previous sublist, we have to use the last node of the sublist before and point
its next pointer to the beginning of the sublist we just reversed. This is the prev pointer. We can use the beforeSubList pointer
we saved earlier and set its next value to prev. We renamed prev to lastOfOGSublist to make it make more sense. You can think
lastOfOGSublist as the last node of the sublist we just reversed but before reversing(once reversed this node would be at the
beginning of the sublist). However, an edge case is that there was nothing before the currentSublist. In that case, beforeSubList
would be None and prev/lastOfOGSublist would actually be set to head.

The next connection we have is the first of the original sublist(before we just reversed) and connecting to the next point of that to
curr. We know curr is pointing to the node right after the sublist we just reversed. As a result, we take the node that
was the first of the sublist before reversing(as now it should be at the end) and point it's next pointer to current.

Lastly, to ensure we can keep on traversing and reversing more groups we have to reset the prev and curr pointer so they are assigned
correctly next time. We know that curr is at the right place as it is at the beginning of the next sublist we want to reverse. However,
prev is not at the right place. Prev should be right before curr. Right now, prev just got reassigned to the beginning of the next
sublist, so it is not right before curr anymore. However, we still have a pointer that points to the end of the reversed sublist(this
was also the beginning of the original sublist). We called this pointer firstOfOGSublist and saved it before we reversed the sublist.
Now, firstOfOGSublist is the pointing to the node right before curr, so we just end up setting prev to firstOfOGSublist.

Time Complexity: O(N) - We process each node a maximum of one times.
Space Complexity: O(1) - No extra space is used.
'''


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
