# (c) 2015 - 2023 Open Risk (https://www.openriskmanagement.com)

from scipy import stats
from scipy.stats import norm

r = norm()
r.cdf(0)  # 0.5
r.mean()  # 0.0
r.ppf(0)  # -inf (inverse cumulative)
