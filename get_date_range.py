import pandas as pd
from utils.validate_date import validate

stocks = pd.read_csv("data/Stocks.csv")
stocks.drop_duplicates(subset=None, inplace=True)

# concat ticker col and dividend col
div = stocks["Next Dividend"]
tick = stocks["ticker"]
date_df = pd.concat([tick, div], axis=1).drop_duplicates().reset_index(drop=True)

# convert string dates to datetime
date_df["Next Dividend"] = pd.to_datetime(date_df["Next Dividend"], dayfirst=True)


def date_range(date_1, date_2):

    validate(date_1)
    validate(date_2)

    start_date = (date_1[0:4]+'_'+date_1[5:7]+'_'+date_1[8:10])

    mask = (date_df["Next Dividend"] > date_1) & (date_df["Next Dividend"] <= date_2)
    final_df = date_df.loc[mask]

    if final_df.empty:
        print("Range must be greater than 0")
    else:
        final_df.to_csv(f"exports/date_range/{start_date}.csv", index=False)
        print('File exported')
