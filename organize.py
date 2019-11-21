# -*- coding:utf8 -*-
import pandas as pd,os

def grounpfile(filename,homepath):
    pf=pd.read_excel(filename,sheet_name= 'FEMA Declarations',header=2,index_col=None)
    os.chdir(homepath)
    os.chdir('./new')
    pf_sorted = pf.groupby(by='Incident Type', as_index=False)
    for key,group in pf_sorted:
        # print("{}\n{}".format(key,group))
        key="{}.csv".format(key.replace('/',' '))
        # print(key)
        group.to_csv(key, index=0)

if __name__=='__main__':
    homepath=os.getcwd()
    if not os.path.exists("original"):
        os.mkdir("original")
    if not os.path.exists("new"):
        os.mkdir("new")
    # os.chdir(homepath)
    os.chdir("./original")

    lisfile=os.listdir()
    print(lisfile)
    for file in lisfile:
        if 'xlsx' in file:
            grounpfile(file,homepath)
