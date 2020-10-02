'''
    Probem Task : Program to calculate the total profit made for the given inputs
    Problem Link : https://edabit.com/challenge/YfoKQWNeYETb9PYpw
    Contributor: https://github.com/anshik1998
'''


class ProfitCalculator:

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def calculate(self):
        # Retrieving the given data from the dictionary

        cost_price = self.dictionary["cost_price"]
        selling_price = self.dictionary["sell_price"]
        inventory = self.dictionary["inventory"]

        # Calculating the total profit made
        profit = (selling_price - cost_price) * inventory

        return profit


if __name__ == "__main__":
    # Creating a dictionary titled 'profit'

    profit = {}

    # Asking user to enter the following data:
    profit["cost_price"] = abs(float(input("Enter the cost price: ")))
    profit["sell_price"] = abs(float(input("Enter the selling price: ")))
    profit["inventory"] = abs(float(input("Enter the total inventory: ")))

    # For the preinput values, uncomment below lines and comment the above profit dictionary.

    #     profit = {
    #         "cost_price" : 32.67,
    #         "sell_price" : 45.00,
    #         "inventory" : 1200
    #     }

    # Calling the class 'ProfitCalculator' and providing the input data in form of dictionary titled 'profit'
    profit_in_dollar = ProfitCalculator(profit)

    # Printing the total profit made by calling class function 'calculate'
    print(round(profit_in_dollar.calculate(), 2))
