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

import numpy as np


# calculate total exposure
def exposure(portfolio):
    return np.sum(portfolio)


# calculate portfolio exposure weights
def weights(portfolio):
    return np.true_divide(portfolio, exposure(portfolio))


# calculate the concentration ratio
def cr(weights, n):
    return weights[:n].sum()


# calculate the normalized hhi concentration index
def hhi(weights):
    n = weights.size
    h = np.square(weights).sum()
    return (h - 1.0 / n) / (1.0 - 1.0 / n)


# calculate the inverted Hannah Kay index
def hk(weights, a):
    n = weights.size
    h1 = np.power(weights, a).sum()
    h2 = np.power(h1, 1.0 / (a - 1.0))
    return (h2 - 1.0 / n) / (1.0 - 1.0 / n)


# calculate the Gini index
def gini(weights):
    n = weights.size
    i = np.arange(1, n + 1)
    return (1.0 - 2.0 * np.multiply(i, weights).sum()) / n + 1.0


# calculate the Shannon entropy index
def shannon(weights):
    weights_nz = weights[weights != 0]
    n = weights_nz.size
    logweights = np.log(weights_nz)
    h = - np.multiply(weights_nz, logweights).sum()
    return 1.0 - h / np.log(n)
