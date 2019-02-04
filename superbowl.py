import pandas as pd
import matplotlib.pyplot as plt
from numpy import array

#Work done by Jason Krasavageo on 2/1/2019
'''function for smoothing out an array of data, making it easier to read
originally created by Randal Olson, grabbed from http://www.randalolson.com/'''
def sliding_mean(data_array, window=1):  
    data_array = array(data_array)  
    new_list = []  
    for i in range(len(data_array)):  
        indices = range(max(i - window + 1, 0),  
                        min(i + window + 1, len(data_array)))  
        avg = 0  
        for j in indices:  
            avg += data_array[j]  
        avg /= float(len(indices))  
        new_list.append(avg)      
    return array(new_list)


'parsing and handling data'
data = pd.read_csv("dataset.csv")
years = []
wins = []
losses = []
for index, row in data.iterrows():
    year = row["Date"][:4]
    win, loss = row["Result"][2:].split("-")
    years.append(int(year))
    wins.append(int(win))
    losses.append(int(loss))
wins = sliding_mean(wins)
losses = sliding_mean(losses) 

print(years)
'''plot stuff'''
plt.figure(figsize=(12, 5))
plt.xlim(1968, 2017)
plt.xticks(range(1968, 2019, 2))
ax = plt.axes()        
ax.xaxis.grid()
#for rotating xaxis labels
plt.setp(ax.get_xticklabels(), rotation=80, horizontalalignment='right') 
plt.title("Point Differential of Superbowl Games", fontsize=22)
plt.plot(years, wins, color='green', label='wins')
plt.plot(years, losses, color='red', label = 'losses')
#filling the gap between win and loss line
plt.fill_between(years, wins, losses, color='#7c91a8')
plt.xlabel('Year', fontsize=18)
plt.ylabel('Points per Game', fontsize=16)
plt.legend()
plt.savefig('superbowl.jpg')
plt.show()

