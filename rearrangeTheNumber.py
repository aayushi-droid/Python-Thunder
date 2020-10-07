'''
    Problem Task : Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.
    Problem Link : https://edabit.com/challenge/jwzAdBnJnBxCe4AXP
'''


def maximumNum(num): 
  
    # Hashed array to store count of digits 
    count = [0 for x in range(10)] 
  
    # Connverting given number to string 
    string = str(num) 
  
    # Updating the count array 
    for i in range(len(string)): 
        count[int(string[i])] = count[int(string[i])] +  1
  
    # Result stores final number 
    result = 0
    multiplier = 1
  
    # traversing the count array 
    # to calculate the maximum number 
  
    for i in range(10): 
        while count[i] > 0: 
            result = result + ( i * multiplier ) 
            count[i] = count[i] - 1
            multiplier = multiplier * 10
  
    # return the result 
    return result
    
def minNum(num):

  #initialize frequency of each digit to Zero 
  freq=[0 for x in range(10)] 
  
  #count frequency of each digit in the number 
  while (num):
    d = num % 10 # extract last digit 
    freq[d]++ #increment counting 
    num = num / 10 #remove last digit 
    
  
  #Set the LEFTMOST digit to minimum expect 0
  result = 0
  for i in range(0,10): 
    
    if (freq[i]):
      result = i 
      freq[i]-- 
      break 
         
     
  
    // arrange all remaining digits 
    // in ascending order 
  for i in range(0,10): 
    while (freq[i]--):
      result = result * 10 + i 
  
    return result
    
def rearrangeNumber(num):
  return maximumNum(num)-minNum(num)
  
  
 
    
    
