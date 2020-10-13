'''
Problem Task: Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:
 - Form the fullname by simply joining the first and last name together, separated by a space.
 - Form the email by joining the first and last name together with a "." in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.

Problem Link: https://edabit.com/challenge/gB7nt6WzZy8TymCah
'''

class Employee:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if isinstance(val, str):
            val = str(val.capitalize())
            self._name = val
        else:
            raise Exception('Invalid name!')

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, val):
        if isinstance(val, str):
            val = str(val.capitalize())
            self._lastname = val
        else:
            raise Exception('Invalid lastname!')

    def fullname(self):
        data = [self.name, self.lastname]
        fullname = ' '.join(data)
        return fullname
    
    def email(self):
        email = (self.name + '.' + self.lastname + '@company.com').lower()
        return email
