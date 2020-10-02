# author : @gittygupta 
'''
Problem description : returns power from input voltage and current values
Problem link : https://edabit.com/challenge/v5gc8FQkDEepkqpfp
'''
def power(v, i):
  return v * i

if __name__ == '__main__':
  print(power(int(input("voltage:")), int(input("current:")) ))
