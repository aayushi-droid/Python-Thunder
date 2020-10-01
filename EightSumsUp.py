# author : @gittygupta
'''
    Probem Task : Eight Sums Up
    Problem Link : https://edabit.com/challenge/ZkWSacTDQ65A3gh6j
'''
def sum_eight(a):
  x = [ [[a[i], a[j]] for i in range(j + 1, len(a)) if (a[i] + a[j]) == 8] for j in range(len(a)) ]
  return [sorted(i[0]) for i in x if i != []]
  
 if __name__ == '__main__':
  print('{"pairs":' + str(sum_eight(list(map(int, input("List : ").split())))) + '}')
