# (c) 2015 - 2023 Open Risk (https://www.openriskmanagement.com)

import json
import numpy as np

filehandle = open("portfolio2.json", "r")
json_data = filehandle.read()
data = json.loads(json_data)

x = np.array(data['Exposure'])
