'''
Problem Statement: Create a function that takes two arguments: the final price and the discount percentage as integers and returns the final price after the discount.

Problem Link: https://edabit.com/challenge/L4Hevck84exPwe4wo

'''

function dis(price, discount) {
	price_after_discount = price - (discount / 100) * price
	return +(price_after_discount).toFixed(2)
}
