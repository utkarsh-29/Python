# Import cars data
import pandas as pd
filePath = "s3://mys3utkbucket/baddrivers.csv"
df = pd.read_csv(filePath)
print(df)
