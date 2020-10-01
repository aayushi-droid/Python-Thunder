'''
    Probem Task : This program implements a recursive function that takes two parameters, an integer n and a string txt, and repeats the string n number of times
    Problem Link : https://edabit.com/challenge/QKmETue6fMTdcB8Rq
'''
*/

def recursionRepeatString(txt,n):
  if(n<= 0):
    return ''
  if(n==1)
    return txt
  if(n>1)
    return txt+recursionRepeatString(txt,n-1)
  
