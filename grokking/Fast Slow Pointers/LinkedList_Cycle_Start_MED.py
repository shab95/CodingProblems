class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_cycle_start(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    if fast == None or fast.next == None:
        return None


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
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
