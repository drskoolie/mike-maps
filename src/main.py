## Part 0: Initialization
import os
import pandas as pd

data_directory = 'data/raw/pollbypoll_bureauparbureauCanada/'
polls = os.listdir(data_directory)
for poll in polls:
    if poll[:5] != 'table':
        print(poll)

df = pd.read_csv(data_directory + polls[0])
df
