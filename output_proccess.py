import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#%% DataFrame Creation
dev1 = pd.read_csv('mnist_01_dev1.csv')
dev2 = pd.read_csv('mnist_01_dev2.csv')

a = list(dev1)
for i in range (len(a)):
    print(a[i], '\n')

def plot_func(category, ylabel, xlabel, title):
    plt.plot(dev1['timestamp'], dev1[category], color = 'blue')
    plt.plot(dev1['timestamp'], dev2[category], color = 'orange')

    #Select Time interval
    num_ticks = 25  # Adjust the number of ticks as needed
    plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(num_ticks))
    plt.xticks(rotation='30')

    #Plot Title and Legend
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    plt.title(title)
    plt.show()