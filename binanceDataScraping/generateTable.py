# import json file and generate table
import pandas as pd
import json
import os

with open('reducedRiskBracketsData.json', 'r') as f:
    data = json.load(f)


# export to csv named by key (symbol)
for key in data:
    df = pd.DataFrame(data[key])
    print(df.head())
    df.to_csv('./binanceDataCSV/{}.csv'.format(key), index=False)

