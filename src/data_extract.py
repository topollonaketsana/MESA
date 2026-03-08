import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

# read the data from the sta output
d1= "../tutorial/star-work/work/LOGS/profile"
d2= "../tutorial/star-work/work/LOGS/history.data"


df1= pd.read_csv(d1 + '1.data', sep= r'\s+', engine= 'python', skiprows= 5)
df2= pd.read_csv(d1 + '2.data', sep= r'\s+', engine= 'python', skiprows= 5)
df3= pd.read_csv(d1 + '3.data', sep= r'\s+', engine= 'python', skiprows= 5)
df4= pd.read_csv(d1 + '4.data', sep= r'\s+', engine= 'python', skiprows= 5)
df5= pd.read_csv(d1 + '5.data', sep= r'\s+', engine= 'python', skiprows= 5)
df6= pd.read_csv(d1 + '6.data', sep= r'\s+', engine= 'python', skiprows= 5)



print(df1.head(), '\n')


# joining them together
df = pd.concat([df1, df2, df3, df4, df5, df6], ignore_index=True)

print(df.head())
