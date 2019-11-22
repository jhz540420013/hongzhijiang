import matplotlib.pyplot as plt
import pandas as pd

def plot():
    df = pd.read_csv('original.csv',sep=',',header=0, usecols=[5])
    df = df.dropna()
    s = pd.Series(df['State '])
    s = s.value_counts()
    s = s.sort_index()
    first =s[0:24]
    second = s[25:]