''' Perfect Sum Problem
Input: arr = [5, 10, 12, 13, 15, 18], K = 30
Output: {12, 18}, {5, 12, 13}, {5, 10, 15}
Explanation: 
Subsets with sum 30 are:
12 + 18 = 30
5 + 12 + 13 = 30
5 + 10 + 15 = 30

Input:  [1, 2, 3, 4], K = 5
Output: {2, 3}, {1, 4}
'''
# A Dynamic Programming solution for subset sum problem 
# Returns true if there is a subset of 
# set[] with sum equal to given sum 

# Returns true if there is a subset of set[] 
# with sum equal to given sum 
def isSubsetSum(set, n, sum): 
	
	# The value of subset[i][j] will be 
	# true if there is a 
	# subset of set[0..j-1] with sum equal to i 
	subset =([[False for i in range(sum + 1)] 
			for i in range(n + 1)]) 
	
	# If sum is 0, then answer is true 
	for i in range(n + 1): 
		subset[i][0] = True
		
		# If sum is not 0 and set is empty, 
		# then answer is false 
		for i in range(1, sum + 1): 
			subset[0][i]= False
			
		# Fill the subset table in botton up manner 
		for i in range(1, n + 1): 
			for j in range(1, sum + 1): 
				if j<set[i-1]: 
					subset[i][j] = subset[i-1][j] 
				if j>= set[i-1]: 
					subset[i][j] = (subset[i-1][j] or
								subset[i - 1][j-set[i-1]]) 
	
		# uncomment this code to print table 
		for i in range(n + 1): 
		for j in range(sum + 1): 
		print (subset[i][j], end =" ") 
		print() 
	return subset[n][sum] 
		
# Driver program to test above function 
if __name__=='__main__': 
	set = [3, 34, 4, 12, 5, 2] 
	sum = 9
	n = len(set) 
	if (isSubsetSum(set, n, sum) == True): 
		print("Found a subset with given sum") 
	else: 
		print("No subset with given sum") 
		
