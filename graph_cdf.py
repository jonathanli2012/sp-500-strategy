import matplotlib.pyplot as plt
import numpy as np

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

def graph_multiple_cdf(d, legend):
    parsed_data = []
    for i in d:
        parsed_data.append(sort_cdf_data(i))
    
    for i in range(len(d)):
        plt.plot(parsed_data[i][0],parsed_data[i][1], label=legend[i])

    plt.xticks(np.arange(0, 8, 0.5))
    plt.yticks(np.arange(0, 1.05, 0.05))
    plt.ylabel('CDF')
    plt.xlabel('Earning Multiples')
    plt.legend(loc="lower right")
    plt.grid()
    plt.show()