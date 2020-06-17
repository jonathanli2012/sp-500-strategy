import matplotlib.pyplot as plt
import numpy as np
import math

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

def get_largest_val(d):
    val = 0
    for i in d:
        for j in i:
            if(j > val):
                val = j
    return val

def get_spacing(max):
    spacing = 0.0
    if (max < 3):
        spacing = 0.05
    elif (max < 5):
        spacing = 0.1
    elif (max < 10):
        spacing = 0.25
    elif (max < 21):
        spacing = 0.5
    elif (max < 31):
        spacing = 1
    elif (max < 100):
        spacing = 2
    elif (max < 200):
        spacing = 4
    elif (max < 350):
        spacing = 10
    else:
        spacing = 16
    return spacing

def graph_multiple_cdf(d, legend):
    parsed_data = []
    for i in d:
        parsed_data.append(sort_cdf_data(i))
    
    for i in range(len(d)):
        plt.plot(parsed_data[i][0],parsed_data[i][1], label=legend[i])

    max = math.ceil(get_largest_val(d))

    title = "CDF of SPX returns from all entry points"
    plt.suptitle(title, fontsize=12)
    plt.xticks(np.arange(0, max + get_spacing(max), get_spacing(max)))
    plt.yticks(np.arange(0, 1.05, 0.05))
    plt.ylabel('CDF')
    plt.xlabel('Earning Multiples')
    plt.legend(loc="lower right")
    plt.grid()
    plt.show()