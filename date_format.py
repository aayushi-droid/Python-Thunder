#easy method 1

import datetime
import argparse

def date_format_changer(args):
	return datetime.datetime.strptime(args.date,'%m/%d/%Y').strftime("%Y%m%d")

parser = argparse.ArgumentParser(description="date format changer")
parser.add_argument('--date',help="give the date inthe format '%m/%d/%Y'")
args = parser.parse_args()
print(date_format_changer(args))
