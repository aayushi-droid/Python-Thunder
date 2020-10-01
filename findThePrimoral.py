#Just enter the number of prime number you want to multiply and you can get the results
#Problem statement: A Primorial is a product of the first n prime numbers (e.g. 2 x 3 x 5 = 30). 2, 3, 5, 7, 11, 13 are prime numbers. 
#If n was 3, you'd multiply 2 x 3 x 5 = 30 or Primorial = 30.
#Problem Link: https://edabit.com/challenge/fRjfrCYXWJAaQqFXF

def find_the_primoral(n):
    s = 2
    p = 1
    a = 0
    while a < n:
        for i in range(2, s):
            if s % i == 0:
                break
        else:
            p = p * s
            a = a + 1
        s = s + 1
    print(p)


n = int(input("enter value of n"))
find_the_primoral(n)
