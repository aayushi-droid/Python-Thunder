"""
Problem Task: This program will add two numbers
Problem link: https://edabit.com/challenge/SFzHtm63XT6EYNHWY
"""


def balance(alist):
    left=0
    right=0
    if len(alist)%2 != 0:
        for i in range(len(alist)//2):
            left+=alist[i]
        for j in range((len(alist)//2)+1,len(alist)):
            right+=alist[j]


    if right>left: return "right"
    elif left>right: return "left"
    return "balanced"

print(balance([0,0,'I',1,1]))
# 0 < 2 so it will tip right
print(balance([1,2,3,4,'I',1,4,0,0]))
# 6 > 4 so it will tip left 
print(balance([5,5,5,0,'I',10,2,2,1]))
# 15=15 so it will stay balanced
