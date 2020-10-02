#problem statement:Power Calculator
#problem link:https://github.com/Py-Droid/Python-Thunder/issues/113
#link:https://edabit.com/challenge/v5gc8FQkDEepkqpfp
# this code Creates a function that takes voltage and current and returns the calculated power.

def circuit_power(vol, current):

    power = float(vol) * float(current)
    return power

print(circuit_power(5, 6))