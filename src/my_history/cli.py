import pandas as pd
import sys

def cnt():
    ind = sys.argv[1]
    df = pd.read_parquet("~/tmp/history.parquet")
    fdf = df[df['cmd'].str.contains(ind)]
    cnt = fdf['cnt'].sum()
    print(cnt)




