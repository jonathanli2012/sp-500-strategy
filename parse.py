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
    
dd = []

for d in data_csv:
  print(d)
  dd.append(stock_val(d))

print(dd[100])

for ddd in dd:
  print(ddd)

