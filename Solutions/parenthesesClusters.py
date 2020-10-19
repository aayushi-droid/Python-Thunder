'''
  Probem Task :
  Write a function that groups a string into parentheses cluster.
  Each cluster should be balanced. for e.g.

  split("()()()") ➞ ["()", "()", "()"]
  split("((()))") ➞ ["((()))"]

  Problem Link : https://edabit.com/challenge/Fpymv2HieqEd7ptAq
'''

def split(txt):
  '''
    Logic: The solution uses a stack to find clusters by looping through the
    string and pushing opening parentheses '(' to the stack and removing
    them when we encounter their respective closing parentheses ')'.

    A balanced cluster will end when all the parentheses will match up
    and hence the stack will then be empty. We will then continue to
    loop over the remaining part of the string.
  '''

  stack = []
  clusters = []  # to store the clusters

  # Starting and ending indexes of cluster
  cluster_start = 0
  index = 0

  # Loop through the contents of txt
  for char in txt:

    if char == '(':   # push every '(' to the stack
      stack.append(char)
    elif char == ')' and stack[-1] == '(':  # and pop the last '(' if an ')' is encountered
      stack.pop()
    else:
      # push ')' to stack if it does not have a opening parentheses
      stack.append(')')
    index += 1

    # When the stack is empty, a cluster is found, add it to the clusters list
    if len(stack) == 0:
        if index >= len(txt):
            clusters.append(txt[cluster_start:])
            break
        clusters.append(txt[cluster_start:index])

        cluster_start = index   # Set cluster_start to after the ending index of current cluster

  return clusters

if __name__ == "__main__":
  string = "(())()()"
  print(f"Parentheses Clusters of '{string}' are {split(string)}")
