class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		# Complete the code!
		self.fullname = firstname + " " + lastname
		self.email = firstname.lower() + "." + lastname.lower() + "@company.com"
		
