'''

Problem Statement: Create a function that builds a word from the scrambled letters contained in the first list. Use the second list to establish each position of the letters in the first list. Return a string from the unscrambled letters (that made-up the word).

Problem Link: https://edabit.com/challenge/R5F99DeuhqYxbGyMM

'''

def wordBuilder(scrambled,sequence):
    
    unscrambled = ""
    
    sequence = list(map(int, sequence))

    for i in sequence:
        unscrambled = unscrambled + scrambled[i]

    return(unscrambled)


scrambledWord = list(input("Input a scrambled word : "))
unscrambleSequence = list(input("Input the sequences of indexes to unscramble the word : "))

unscrambledWord = wordBuilder(scrambledWord,unscrambleSequence)

print("The unscrambled word is '{}'.".format(unscrambledWord))

