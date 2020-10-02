# this code Creates a function that takes voltage and current and returns the calculated power.

def circuit_power(vol, current):

    power = float(vol) * float(current)
    return power

print(circuit_power(5, 6))