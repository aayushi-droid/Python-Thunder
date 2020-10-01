'''
    Probem Task : Create a function that returns the Primorial of a number
    Problem Link : https://edabit.com/challenge/fRjfrCYXWJAaQqFXF
'''
def isPrime(n) :

    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

def primorial(n):
        ans = 2
        pri = 3
        #cnt = n
        if n==1:
                return 2
        while n>1:
                if isPrime(pri):
                        print("Prime number is"+str(pri))
                        ans = ans*pri
                        #print("Next answer is"+str(ans))
                        n = n-1
                pri = pri+2
        return ans
