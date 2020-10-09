'''
    Problem statement: Create the instance attributes fullname and email in the Employee class.
                       Given a person's first and last names:

                       - Form the fullname by simply joining the first and last name together,
                         separated by a space.
                       - Form the email by joining the first and last name together with a "." in between,
                         and follow it with @company.com at the end.
                         Make sure the entire email is in lowercase.
    Problem Link: https://edabit.com/challenge/gB7nt6WzZy8TymCah
'''

class Employee:
    
    def __init__(self, firstname:str, lastname:str)->None:
        self.firstname = str(firstname) if firstname else ""
        self.lastname = str(lastname) if lastname else ""
        self.data = [self.firstname, self.lastname]

    def fullname(self)->str:
        return ' '.join(self.data)
	
    def email(self)->str:
        return ('.'.join(self.data) + '@company.com').lower()
		
    def get_firstname(self)->str:
        return self.firstname

    def get_lastname(self)->str:
        return self.lastname