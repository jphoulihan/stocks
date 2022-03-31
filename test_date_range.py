import pandas as pd
from get_date_range import date_range

stocks = pd.read_csv("data/Stocks.csv")
stocks.drop_duplicates(subset=None, inplace=True)

stocks["Next Dividend"] = pd.to_datetime(stocks["Next Dividend"], dayfirst=True)

count = 0
while count < 5: #number of test input to be run

    date_1 = stocks["Next Dividend"].sample().to_string(index=False)
    date_2 = stocks["Next Dividend"].sample().to_string(index=False)

    print("Date search: ", date_1, "-", date_2)
    date_range(date_1, date_2)
    print("\n")
    count += 1
