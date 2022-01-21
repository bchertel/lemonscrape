import pandas as pd
import os

#Get newest WMTM data file
def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)


new = newest(os.path.join(os.getcwd(),"data"))

#Read csv file to pandas DataFrame
df1 = pd.read_csv(new)

#Sort column headers
df1 = df1.sort_index(axis=1)

#Sort product 'repository-id' values
df1 = df1.sort_values(by=['repository-id'])

#Show brief output
print(df1)
df1.to_csv("test.csv")

