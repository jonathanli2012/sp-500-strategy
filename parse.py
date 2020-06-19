import csv

data = []

data_file = open("data.csv")
data_csv = csv.reader(data_file)

class stock_val:
  def __init__(self, d):
    self.date = d[0]
    self.open = float(d[1])
    self.high = float(d[2])
    self.low = float(d[3])
    self.close = float(d[4])
    self.adj_close = float(d[5])
    self.volume = float(d[6])
    
  def __str__(self):
    return str(self.date) + " " + str(self.open) + " " + str(self.high) + " " + str(self.low)

for d in data_csv:
  data.append(stock_val(d)) 

closes = []
date = []

for d in data:
  closes.append(d.adj_close)
  date.append(d.data)

"""
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
plt.plot(closes, '-o', markersize=1)
plt.show()
"""
