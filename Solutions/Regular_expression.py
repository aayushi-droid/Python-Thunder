""" A regular experssion is a sequence of character that defines a search pattern"""
import re

pattern = (
    "^a...e$"  # it will find a string start with 'a' and end with 'e' with 5 letters
)
test_string = "apple"

result = re.match(pattern, test_string)

if result:
    print("Serach Successful")
else:
    print("Seaching Fail")
