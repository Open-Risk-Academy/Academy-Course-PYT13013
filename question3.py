# (c) 2015 - 2025 Open Risk (https://www.openriskmanagement.com)
#
# This code is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of the course. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

import json

import numpy as np

# import the required modules
# use a convenient alias to reduce typing
import concentration_library as cl

# load the JSON data and parse it into a dictionary
filehandle = open("portfolio2.json", "r")
json_data = filehandle.read()
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
hk = cl.hk(weights, 3)

# print out the values
print("HHI: ", hhi)
print("Gini: ", gini)
print("Shannon: ", shannon)
print("HK: ", hk)
