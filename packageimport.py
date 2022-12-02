import pandas as pd
import os

os.chdir('C:\\Users\\stevi\\OneDrive\\Desktop\\py2exe')

df = pd.read_csv('SocialNetworkingTwoData.csv')

print(df.head(10))