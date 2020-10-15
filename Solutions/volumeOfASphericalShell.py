'''
    Probem Task : This program will find volume of inner sphere
    Problem Link : https://edabit.com/challenge/iBqJcagS56wmDpe4x
'''
def vol_shell(r1, r2):  # function for finding volume
    pi = 3.1415926536
    if r1 < r2:  # Checking is r1 is greater than r2, if r1 is less than r2, if case works
        r1, r2 = r2, r1
        volume = 4 / 3 * pi * (int(r1) ** 3 - int(r2) ** 3)  # main formulae
        print(round(volume, 3))  # Printing the value,
        # round is Used for rounding the digits of volume to 3 digits from decimal point
    else: # if r1 is greater than r2, this case executes
        volume = 4 / 3 * pi * (int(r1) ** 3 - int(r2) ** 3)  # main formulae
        print(round(volume, 3))  # Printing the value,
        # round is Used for rounding the digits of volume to 3 digits from decimal point


if __name__ == '__main__':  # Main Function
    r1 = input("Input Inner/Outer radius of the sphere: ")
    r2 = input("Input Inner/Outer radius of the sphere: ")
    vol_shell(r1, r2)
