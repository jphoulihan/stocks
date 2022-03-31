import pandas as pd
import random
from get_by_id import get_stock_json

stocks = pd.read_csv("data/Stocks.csv")

id_list = [i for i in stocks.columns[:4]] #gen list of stock identifier names

count = 0
while count < 5: #number of test input to be run

    test_list = []
    test_input = stocks[id_list[random.randint(0, 3)]].sample().to_string(index=False) #gen id name and sample row
    print("ID search: ", test_input)
    get_stock_json(test_input, True)
    print("\n")
    count += 1
