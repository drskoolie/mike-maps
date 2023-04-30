## Part 0: Initialization
import os
import pandas as pd

data_directory = "data/raw/pollbypoll_bureauparbureauCanada/"
polls = os.listdir(data_directory)


## Part 1: Column Renaming
df = pd.read_csv(data_directory + polls[0])

columns_original = [
    "Electoral District Number/Numéro de circonscription",
    "Electoral District Name/Nom de circonscription",
    "Polling Station Number/Numéro du bureau de scrutin",
    "Polling Station Name/Nom du bureau de scrutin",
    "Rejected Ballots/Bulletins rejetés",
    "Total Votes/Total des votes",
    "Electors/Électeurs",
]

columns_condensed = [
    "District Number",
    "District Name",
    "Polling Number",
    "Polling Name",
    "Rejected Ballots",
    "Total Votes",
    "Electors",
]

columns_dict = dict(zip(columns_original, columns_condensed))
df = df.rename(columns=columns_dict)
df = df.rename(str.lower, axis='columns')

df.columns

df.iloc[:,5].sum()

# Part 2: Iterating
for poll in polls:
    if poll[:5] != "table":
        pass
