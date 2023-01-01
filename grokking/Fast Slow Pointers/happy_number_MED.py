'''
Problem Statement 
Any number will be called a happy number if, 
after repeatedly replacing it with a number equal to the sum of the square of all of its digits, 
leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. 
Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
'''

# mycode


def find_happy_number(num):
    slow, fast = num, get_next_number(num)
    while (slow != fast and fast != 1):
        slow = get_next_number(slow)
        fast = get_next_number(get_next_number(fast))
    return fast == 1


def get_next_number(num):
    sum = 0
    while num != 0:
        digit = num % 10
        sum += digit ** 2
        num = num // 10
    return sum


'''
Summary:

The problem requires the application of the fast slow pointers technique. We have to think of the process of getting the sum of squares
constantly as a cycle. It gives us a cycle of numbers. The cycle will lead us to one or it will lead us to a number we have gotten
before. If the cycle gets us to 1, then we know it's a happy number. The fast pointer will likely get there first, since it's going
through the cycle at twice the speed. However, if we reach a number that we have gotten before that's not 1, then we know the cycle 
will never lead us to 1. That's how we know it's not a happy number. The slow pointer starts at the num and the fast pointer can
start at the sum of the squares of num. It doesn't matter where fast and slow start as long they both start at some point in the cycle.

Time Complexity: O(logN) - The time complexity of the algorithm is difficult to determine. However we know the fact that all unhappy numbers eventually get stuck in the cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4

                            This sequence behavior tells us two things:

                            1)If the number Nis less than or equal to 1000, then we reach the cycle or '1' in at most 1001 steps.
                            
                            2)For N > 1000, suppose the number has 'M' digits and the next number is 'N1'. 
                            From the above Wikipedia link, we know that the sum of the squares of the digits of 'N' is at most 9^2 M, 
                            or 81M81M (this will happen when all digits of 'N' are '9'). 
                            
                            This means:

                            N1 < 81M
                            As we know M = log(N+1)
                            Therefore: N1 < 81 * log(N+1) => N1 = O(logN)
                            This concludes that the above algorithm will have a time complexity of O(logN).

Space Complexity: O(1) - No additional space is required.

***NOTE***
Another simple way to solve this problem is by using hashes. If we see a number that is already hashed that is not 1, then we know we are
in a cycle and can return that it is not a happy number. However, the space complexity for this would be O(N).

'''


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
