def fact(n):
    fct = 1
    for i in range(1,n + 1):
        fct = fct*i
    return(fct)
		
print("fact(0)",fact(0))
print("fact(1)",fact(1))
print("fact(2)",fact(2))
print("fact(3)",fact(3))
print("fact(7)",fact(7))
print("fact(9)",fact(9))
print("fact(15)",fact(15))
