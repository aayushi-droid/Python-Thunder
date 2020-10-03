# '''
# Abigail and Benson are playing Rock, Paper, Scissors.

# Each game is represented by an array of length 2, where the first element represents what Abigail played and the second element represents what Benson played.

# Given a sequence of games, determine who wins the most number of matches. If they tie, output "Tie".

# R stands for Rock
# P stands for Paper
# S stands for Scissors

# Examples
# calculate_score([["R", "P"], ["R", "S"], ["S", "P"]]) ➞ "Abigail"

# # Ben wins the first game (Paper beats Rock).
# # Abigail wins the second game (Rock beats Scissors).
# # Abigail wins the third game (Scissors beats Paper).
# # Abigail wins 2/3.

# calculate_score([["R", "R"], ["S", "S"]]) ➞ "Tie"

# calculate_score([["S", "R"], ["R", "S"], ["R", "R"]]) ➞ "Tie"


if __name__ == "__main__":
    a = 0
    b = 0
    A = []
    for i in range (3):
        B = []
        for j in range (1):
            B.append(str(input()))
        A.append(B)    
    for i in range (3):
        if A[i][0] == 'R' and A[i][1] == 'P':
            b += 1
        elif A[i][0] == 'R' and A[i][1] == 'S':
            a += 1
        elif A[i][0] == 'P' and A[i][1] == 'S':
            b += 1                                     #After this
        elif A[i][0] == 'P' and A[i][1] == 'R':
            a += 1
        elif A[i][0] == 'S' and A[i][1] == 'R':
            b += 1
        else:
            a += 1
    if a == b:
        print('Abigali wins ' +str(a)+'/3' )
    elif b > a:
        print('Benson wins ' +str(a)+'/3' )
    else:
        print('Tie')     
            
        
