import csv

data = []

data_file = open("data.csv")
data_csv = csv.reader(data_file)

class stock_val:
  def __init__(self, d):
    self.date = d[0]
    self.open = d[1]
    self.high = d[2]
    self.low = d[3] 
    self.close = d[4]
    self.adj_close = d[5]
    self.volume = d[6]
    
  def __str__(self):
    return str(self.date) + " " + str(self.open) + " " + str(self.high) + " " + str(self.low)

for d in data_csv:
  data.append(stock_val(d))

closes = []

for d in data:
  closes.append(float(d.adj_close))

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
plt.plot(closes, '-o', markersize=1)
plt.show()

def years_to_days(x):
  return x*365

gains = []
for i in range(0,len(closes) - years_to_days(25)):
  gains.append(closes[i+years_to_days(25)]/closes[i])

def sort_cdf_data(d):
    vals = []
    for i in d:
        vals.append(i)
    sorted_vals = np.sort(vals)
    y_vals = np.arange(len(sorted_vals))/float(len(sorted_vals)-1)
    return sorted_vals, y_vals

def graph_cdf(d):
    x, y = sort_cdf_data(d)
    title = "CDF"
    fig = plt.figure()
    fig.suptitle(title, fontsize=12)
    plt.ylabel('CDF')
    plt.xlabel('Earning Multiples')
    plt.plot(x, y)
    plt.show()

graph_cdf(gains)