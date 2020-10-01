'''
    Probem Task : This program will unscramble letters from the first list from the positions given in the 2nd list
    Problem Link : https://edabit.com/challenge/R5F99DeuhqYxbGyMM
'''

def unscramble(letters, positions):
  return ''.join(letters[i] for i in positions)

if __name__ == '__main__':
  print(unscramble(list(map(str, input("Letters : ").split())), list(map(int, input("Positions : ").split()))))
