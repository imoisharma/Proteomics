import pandas as pd 
import numpy as np 

# Read the file ProteinGroups.xlsx file

df = pd.read_excel("proteinGroups.xlsx")
print(df.head(10))