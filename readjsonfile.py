# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:45:21 2015

@author: open risk
"""

import json
import numpy as np
filehandle = open("portfolio2.json","r")
json_data= filehandle.read()
data = json.loads(json_data)

x = np.array(data['Exposure'])    