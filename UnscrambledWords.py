def unscramble(letters, positions):
  return ''.join(letters[i] for i in positions)

if __name__ == '__main__':
  print(unscramble(list(map(str, input("Letters : ").split())), list(map(int, input("Positions : ").split()))))
