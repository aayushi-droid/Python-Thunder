"""
    Probem Task  : Given a list with an odd number of elements, return whether the scale will tip "left" or "right" based on the sum of the numbers. The scale will tip on the direction of the largest total. If both sides are equal, return "balanced".
    Problem Link : https://edabit.com/challenge/xPmfKHShmuKL5Qf9u
"""

def balancedScales(array):
    middle_pos = len(array)//2
    left_sum = sum(array[:middle_pos])
    right_sum = sum(array[middle_pos+1:])

    if left_sum > right_sum:
        return "left"
    elif left_sum == right_sum:
        return "balanced"
    else:
        return "right"

if __name__=='__main__': 
    if balancedScales([0, 0, "I", 1, 1]) == "right":
        print("Test case 1 passed")
    if balancedScales([1, 2, 3, "I", 4, 0, 0]) == "left":
        print("Test case 2 passed")
    if balancedScales([5, 5, 5, 0, "I", 10, 2, 2, 1]) == "balanced":
        print("Test case 3 passed")