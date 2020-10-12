'''
	Problem statement: Make a function that encrypts a given input with these steps:Write a function that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that integer written in English.:

	Examples
	num_to_eng(0) ➞ "zero"
	num_to_eng(18) ➞ "eighteen"
	num_to_eng(126) ➞ "one hundred twenty six"
	num_to_eng(909) ➞ "nine hundred nine"
	Notes
	There are no hyphens used (e.g. "thirty five" not "thirty-five").
	The word "and" is not used (e.g. "one hundred one" not "one hundred and one").


Problem Link : https://edabit.com/challenge/mZqMnS3FsL2MPyFMg

'''

def num_to_eng(n):
	n = str(n)
	final_digits = ""
	num_gt_nineteen_lt_ninety_nine = {'1':'one', '2':'twenty', '3':'thirty', '4':'fourty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety', '0':''}
	num_gt_zero_lt_twenty = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'', '10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen', '20':'twenty', '00':''}
	
	if int(n) >= 100:
		if int(n[1:]) >= 10 and int(n[1:]) < 20:
			return num_gt_zero_lt_twenty[n[0]] + " hundred" + " " + num_gt_zero_lt_twenty[n[1:]]
		return (num_gt_zero_lt_twenty[n[0]] + " hundred" + " " + num_gt_nineteen_lt_ninety_nine[n[1]] + " " + num_gt_zero_lt_twenty[n[2]]).replace("  ", " ")
	
	if int(n) > 20 and int(n) < 100:
		return num_gt_nineteen_lt_ninety_nine[n[0]] + " " + num_gt_zero_lt_twenty[n[1]]
	
	if int(n) <= 20:
		if int(n) == 0:
			return "zero"
		return num_gt_zero_lt_twenty[n]
	 
print(num_to_eng(987))
