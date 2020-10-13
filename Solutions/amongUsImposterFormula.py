'''
    Probem Task : This program will calculate the chance of being an imposter.
    Problem Link : https://edabit.com/challenge/b36bBpsnzyDbd4mzF
'''
# function to calculate chance of being an imposter
def imposterChance(imposter, players):
    percentage = 100 * (imposter / players)
    return round(percentage)

def main():
    p = int(input('Enter Number of players in Among Us: '))
    i = int(input('Enter Number of imposters in Among Us: '))
    chance_of_imposter = imposterChance(i, p)
    print(f"The chance for each player of being an imposter is {chance_of_imposter}%")

if __name__ == '__main__':
    main()
