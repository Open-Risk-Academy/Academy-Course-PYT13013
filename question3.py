
# import the require modules
# use a convenient alias to reduce typing
import concentration_library as cl
import json
import numpy as np

# load the JSON data and parse it into a dictionary
filehandle = open("portfolio2.json","r")
json_data= filehandle.read()
data = json.loads(json_data)

# move the data into a numpy array and sort it
portfolio = np.array(data['Exposure'])
portfolio = sorted(portfolio, reverse=True)

# calculate the portfolio weights
weights = cl.weights(portfolio)

# calculate the desired indexes
hhi = cl.hhi(weights)
gini = cl.gini(weights)
shannon = cl.shannon(weights)
hk = cl.hk(weights,3)

# print out the values
print("HHI: ", hhi)
print("Gini: ", gini)
print("Shannon: ", shannon)
print("HK: ", hk)