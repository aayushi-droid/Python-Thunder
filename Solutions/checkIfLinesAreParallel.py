'''
    Problem Task: Check If Two Lines Are Parallel Or Not.
    Problem Link: https://edabit.com/challenge/8rEEHcmq8rRaTksd7
'''
def lines_are_parallel(l1, l2):
	x1 = l1[0]*-1;
	y1 = l1[1];
	x2 = l2[0]*-1;
	y2 = l2[1];
	return (x1/y1 == x2/y2);