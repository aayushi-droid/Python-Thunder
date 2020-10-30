# Question statement :
#https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

# this is the classical Tower of Hanoi Problem, in which:

# We have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
# 1) Only one disk can be moved at a time.
# 2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
# 3) No disk may be placed on top of a smaller disk.

#Algorithm Used : We solve this problem using Recursion.


def toh(n,A,B,C):   # This is the function to shift n disks from A to B using C.
    if n == 0:  # Base case, If all the disks have been moved, move out from the function.
        return
    toh(n-1,A,C,B)   #We shift n-1 disks from A to C using B.
    print('Move',n,'from',A,'to',B)
    toh(n-1,C,B,A)   # We shift n-1 disks from C to B using A.

toh(3,'A','B','C')

# This code is contributed by Kaushalendra Pandey