from parse import *
from graph_cdf import *

def years_to_days(x):
  return x*365

def get_gains_arr(years):
    gains = []
    for i in range(0,len(closes) - years_to_days(years)):
        gains.append(closes[i+years_to_days(years)]/closes[i])

    return gains

data = []
legend = []
for i in range(1, 7, 1):
    legend.append(str(i) + " years")
    data.append(get_gains_arr(i))

graph_multiple_cdf(data, legend)