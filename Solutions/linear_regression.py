from random import randint
from sklearn.linear_model import LinearRegression

#limit under which random integers are
setLimit = 1000

#to create exactly 100 data items
setCount = 100

#lists that contains input and corresponding output
setInput = list()
setOutput = list()

#creating 100 data items with three columns each
for i in range(setCount):
    a = randint(0, setLimit)
    b = randint(0, setLimit)
    c = randint(0, setLimit)
    #creating output for each data items and appending the lists
    output = a + (2 * b) + (3 * c)
    setInput.append([a, b, c])
    setOutput.append(output)

#initializing the linear reg model
predictor = LinearRegression(n_jobs = -1)

#fill the model with data
predictor.fit(X = setInput, y = setOutput)

#random test data
X_test = [[50, 250, 500]]

#predicting outcome and coefficients
outcome = predictor.predict(X = X_test)
coeff = predictor.coef_

print('Outcome : {}\nCoefficients : {}'.format(outcome, coeff))
