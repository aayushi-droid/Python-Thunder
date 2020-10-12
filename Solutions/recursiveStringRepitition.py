'''
    Problem Task : This program creates a recursive function that takes two parameters, string txt and number n, and repeats the string n number of times
    Problem Link : https://edabit.com/challenge/QKmETue6fMTdcB8Rq
'''
*/
def recursiveStringRepetition(txt,n):
  if(n<=0):
    return ''
  if(n==1):
    return txt
  if(n>1):
    return txt+recursiveStringRepetition(txt,n-1)
    
  
