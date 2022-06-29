# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:45:21 2015

@author: open risk
"""

import csv

filehandle = open("portfolio.csv", "r")
reader = csv.reader(filehandle, delimiter=',')
for row in reader:
    print(row[1])
