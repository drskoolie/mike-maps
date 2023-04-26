## Part 0: Initialization
import os
import pandas as pd

data_directory = 'data/raw/pollbypoll_bureauparbureauCanada/'
polls = os.listdir(data_directory)
for poll in polls:
    print(poll)
pd.read_csv('data/raw/pollbypoll_bureauparbureauCanada/pollbypoll_bureauparbureau10001.csv')
