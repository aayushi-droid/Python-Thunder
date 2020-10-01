#Before jumping into Pr first comment for assign.All Problem from Edabit. Link is mandatory to add

#Problem statement: Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

#Examples:

#format_date("11/12/2019") ➞ "20191211"

#format_date("12/31/2019") ➞ "20193112"

#format_date("01/15/2019") ➞ "20191501"

#easy method 1



import datetime
import argparse

def date_format_changer(args):
	return datetime.datetime.strptime(args.date,'%m/%d/%Y').strftime("%Y%m%d")

parser = argparse.ArgumentParser(description="date format changer")
parser.add_argument('--date',help="give the date inthe format '%m/%d/%Y'")
args = parser.parse_args()
print(date_format_changer(args))

###use python3 date.py date '11/12/2019'
