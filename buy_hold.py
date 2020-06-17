from parse import *
from graph_cdf import *

def years_to_days(x):
  return x*365

def get_gains_arr(years):
    gains = []
    for i in range(0,len(closes) - years_to_days(years)):
        gains.append(closes[i+years_to_days(years)]/closes[i])

    return gains

def get_gains_arr_days(days):
    gains = []
    for i in range(0,len(closes) - days):
        gains.append(closes[i+days]/closes[i])

    return gains


data = []
legend = []
yrs = list(range(1, 5, 1))
#yrs = [0.25, 0.5, 0.75, 1]
for i in yrs:
    legend.append(str(i) + " years")
    data.append(get_gains_arr(i))

graph_multiple_cdf(data, legend)



data = []
legend = []
#days = list(range(1, 5, 1))
days = [100, 200, 300]
for i in days:
    legend.append(str(i) + " days")
    data.append(get_gains_arr_days(i))

graph_multiple_cdf(data, legend)
