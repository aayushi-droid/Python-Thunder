Given a positive integer N. 
The task is to find 12 + 22 + 32 + ….. + N2.
Sum of the series

#solution 

def squaresum(n) : 
  
  
    sum = 0
    for i in range(1, n+1) : 
        sum = sum + (i * i) 
      
    return sum 
 # Driven Program 
n = 5
print(squaresum(n)) 
