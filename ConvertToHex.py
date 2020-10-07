def convert_to_hex(txt):
  solution=""
  for chr in txt:
    solution = solution + format(ord(chr), "x") + " "
  return solution[:-1]
