# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:31:38 2015

@author: philippos
"""

from scipy import stats
from scipy.stats import norm

r = norm()
r.cdf(0)  # 0.5
r.mean()  # 0.0
r.ppf(0)  # -inf (inverse cumulative)
