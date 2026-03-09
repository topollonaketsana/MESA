import os
import matplolib.pyplot as plt 
import seaborn as sn
import pandas as pd


# open dataset - profiles simulations
star= pd.read_csv('../extracted_data/profiles.csv')

print(star.head(10))

# data cleaning

