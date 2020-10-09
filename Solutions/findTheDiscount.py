"""
    Create a function that takes two arguments: the final price and the discount as integers and returns the final price after the discount.

    https://edabit.com/challenge/cXnkmRdxqJrwdsP4n
"""

def findTheDiscount(price,discount):
  price = price - ((discount/100)*price)
  return price


print(findTheDiscount(1500, 20))
