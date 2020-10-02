'''
    Probem Task : Creating a program that takes a string and returns a string with its letters arranged in alphabetical order
    Problem Link : https://edabit.com/challenge/4Agr8CTY7x2rAhh5n
    Contributor: https://github.com/anshik1998
'''


class AlphabetSoup:

    def __init__(self, word):
        self.word = word

    def soup(self):
        split_word = [char for char in self.word.lower()]  # Splitting the word
        sorted_char = sorted(split_word)  # Sorted the list of characters
        word_soup = ''.join(sorted_char)  # Joining the sorted characters

        return word_soup


if __name__ == "__main__":
    string = input("Enter the alphabet: ")

    alphabet_soup = AlphabetSoup(string)  # Calling the class 'Alphabet Soup'
    print(alphabet_soup.soup())  # Calling class function 'soup' and printing it
