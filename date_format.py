'''
    Problem Task : Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

    Problem Link : https://edabit.com/challenge/co4nwXSvnCjGEu8vp
'''

def format_date(date):
	return ''.join(date.split('/')[::-1])