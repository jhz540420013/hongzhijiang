import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
import os
# import matplotlibpd
#
#
# matplotlib.rc('font', family='SimHei', weight='bold')
# plt.rcParams['axes.unicode_minus'] = False



# def first_plot(date, value):
#     plt.figure(figsize=(14, 8), dpi=80)
#     plt.plot(value, date)
#     # plt.xticks(rotation=90)
#     plt.grid(alpha=0.4)
#     plt.title('随时间变化事故出现的次数', fontsize=15)
#     plt.xlabel('时间', fontsize=15)
#     plt.ylabel('次数', fontsize=15)
#     for a, b in zip(date, value):
#         plt.text(b, a, b, ha='center', va='bottom', fontsize=15)
#
#     plt.show()

def first_plot(df):
    year = df['Incident Begin Date'].str.split('-', n=1, expand=True)
    df['year'] = year[0]
    df.drop(columns = ['Incident Begin Date'], inplace= True)
    df = pd.Series(df['year'])
    new = df.value_counts()
    new = new.sort_index()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.plot(date, value)
    plt.xticks(rotation=90)
    plt.grid(alpha=0.4)
    plt.title('随时间变化事故出现的次数', fontsize=15)
    plt.xlabel('时间', fontsize=15)
    plt.ylabel('次数', fontsize=15)
    plt.show()



def second_plot(df):
    df = pd.Series(df['State '])
    new = df.value_counts()
    new = new.sort_index()
    x = new.keys()
    y = new.values()
    plt.figure(figsize=(14, 8), dpi=80)
    plt.scatter(x, y)
    plt.title('每年事故出现的次数', fontsize=15)
    plt.xlabel('state', fontsize=15)
    plt.ylabel('次数', fontsize=15)
    plt.show()

def main():
	curr = os.getcwd()
	for r, d, f in os.walk(curr):
	    for file in f:         
	    	if '.csv' in file:
	    		print (file)
	    		df = pd.read_csv(file,sep=',',header=0, usecols=[10])
    			first_plot(date, value)
    # list = Counter([row['State'] for row in pd.read_csv('Flood.csv').iterrows()])
    			data = pd.read_csv(file,sep=',',header=0, usecols=[5])
    			second_plot(data)
    

    # second_plot(datas)


if __name__ == '__main__':
    main()
