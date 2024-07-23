import pandas as pd
import sys

def cnt(ind):
    df = pd.read_parquet("~/tmp/history.parquet")
    fdf = df[df['cmd'].str.contains(ind)]
    cnt = fdf['cnt'].sum()
    print(cnt)

def main():
    ind = sys.argv[1]
    cnt(ind)

if __name__=='__main__':
    main()


