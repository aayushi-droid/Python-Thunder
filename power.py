'''
    Probem Task : Power Calculation
    Problem Link : https://edabit.com/challenge/v5gc8FQkDEepkqpfp
'''

def circuit_power(v,i):
    return v*i
v=int(input('INPUT VOLTAGE'))
i=int(input("INPUT CURRENT"))
print(f"Power is {circuit_power(v,i)}")