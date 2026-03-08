import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

# read the data from the sta output
d1= ("../tutorial/2.star-work/work/LOGS/pgstar.dat")
d2= ("../tutorial/2.star-work/work/LOGS/history.data")

'''
lines= d2.readlines()

for line in lines:
       print(line, end= '')
'''

#df1= pd.read_csv(d2, delim_whitespace=True, skiprows= 5)
df2= pd.read_csv(d2, sep=r"\s+", engine= 'python', skiprows= 6)


df2.head()





