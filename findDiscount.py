'''

    Problem Task : Create a function that takes two arguments: the final price and the discount as integers and returns the final price after the discount.
    Problem Link : https://edabit.com/challenge/L4Hevck84exPwe4wo

'''


def findDiscount(price, discount):

    value = price - (discount/100 * price)
    if value.is_integer():
        return int(value)
    else:
        return round(value, 2)


print(findDiscount(593, 61))
