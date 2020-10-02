'''
Example:
      counterpartCharCode(character) - It will return the ascii value of the counter part of the character.

      counterpartCharCode('A') - returns 97
      counterpartCharCode('c') - returns 67
      counterpartCharCode('B') - returns 98
'''
def counterpartCharCode(char):
  if(char.islower()):
    return (ord(char.upper()))
  else:
    return (ord(char.lower()))

print(counterpartCharCode('B'))