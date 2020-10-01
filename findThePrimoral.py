#Just enter the number of prime number you want to multiply and you can get the results

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
