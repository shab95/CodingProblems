class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_start(head):
    intersection = None
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            intersection = slow
            break

    slow = head
    while (intersection != slow):
        intersection = intersection.next
        slow = slow.next

    return intersection


'''
Summary:

This is a problem that requires the application of two pointers and some math proof to get the final start of the cycle.
Without the proof here's the answer. The first step is to find the intersection of both pointers in the cycle. We will call
this variable the intersection. Now, we put pointer at header and another pointer at the intersection. After increasing the
intersection pointer and the head pointer at one step at a time, they will eventually meet at the start of the cycle.

The reason why they meet at the start can get complex.

Here's a short math proof with some comments:

First let's define some variables:

D = distance from start of the linked list and the start of the cycle(inclusive)
K = distance from start of the cycle to the meeting point(inclusive)
C = length of cycle

First Part - Finding the intersection:
slow pointer distance traveled:
D + K + i * C 
i is the number of times that the slow pointer has gone in the cycle

fast pointer distance traveled:
D + K + j * c
j is the number of times that the fast pointer has gone in the cycle

we also know that the fast pointer has traveled twice the distance of slow pointer, so we can say:
2(D + K + iC) = D + K + jC
2D + 2K + 2iC = D + K + jC
D + K =  C(j - 2i)
D = C(j - 2i) - K

What does this mean?
First understand that j - 2i is just a constant we're dealing with. C multiplied with any number will be just be a multiple of C.
If we are at any point in the cycle and decide to take C * (j-2i) steps, then we're just going to return to the same point.
The second to last statement also tells us that D + K is a multiple of the cycle length size. 

Although, we do not know exactly how much K is, we do know the intersection point is K nodes after the starting point. As a result,
let's place a pointer at the intersection node. We know this pointer is a distance of K from the starting point. If we made this pointer
travel another D spots, then it would get back to the start of the cycle. Why? Because we know D + K is a multiple of the cycle size.
We pretended that our pointer that just traveled D spots, initially already traveled K spots to the intersection point. And then
we traveled another D nodes. 

Now, we know our pointer at the intersection would discover the starting node simply by moving forward D nodes. We still 
do not know what D is and that's basically what we're trying to figure out. However, now we have two key ideas. We know that
D is a number of steps that the intersection pointer can take to get to the starting node. We also know that D is the number of 
steps that a pointer starting from head takes to get to the starting node. As a result, if we start one pointer at the intersection
and one pointer at head, then move each pointer one at a time, they will meet at D points. How?

Moving each pointer one a time basically means we're testing for points of D between 1 and infinity. To make it even simpler,
knowing the fact that each pointer traveling the same distance will get to the start of the cycle, we start testing different 
distances. Since we're dealing with linked lists, the easiest way to do this is by starting at 1 step and increasing.

**NOTE***
It is important to realize that an answer that is much easier to understand is by using one pointer and a hashtable.
Once we find a node with a value that is already hashed, we know that node is the start of the cycle. However, this would require
N space.
'''


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()

# SOLN 1 Time: O(n) Space: O(1)
# s = distance from start to start of loop
# p = distance from start of loop to meeting point
# l = length of loop

# slowPointer = s + l * c + p where c is the number of cycles slowPointer made in the loop
# fastPointer = s + l * y + p where y is the number of cycles fastPointer made in the loop

# fastPointer also traveled doubled the distance slowPointer did so
# fastPointer = 2(s + l*c + p)

# 2s + 2lc + 2p = s + ly + p
# s = ly - 2lc -p
# s = l(y -2c) - p

# logic:
# when slowPtr starts from begining and gets to "s" length that's when it reaches the start of the loop

# (y-2c) * l is just the number of cycles times the length of the loop itself, so traveling this distance will end up
# at the original meeting position if the fastPointer travels from the meeting position. Now, fastPointer is still s distance
# after the loop. Once you subtract p, you end up at the starting distance.


# SOLN 2 Time: O(n) Space: O(n)
# hash all nodes into hm and go until you find a node that's already hashed.
# Note: Hash the nodes, not node values
