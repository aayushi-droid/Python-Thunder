#author : @gittygupta
'''
    Probem Task : This program takes a positive integer and calculates how many dots exist in a pentagonal shape around the center dot on the Nth iteration.
    Problem Link : https://edabit.com/challenge/G9QRtAGXb9Cu368Pw
'''
def pentagon(n):
  return sum([(i-1) * 5 for i in range(2, n+1)]) + 1
  
if __name__ == '__main__':
  print(pentagon(int(input("Enter n : "))))
