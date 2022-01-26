import pandas as pd
import random
from get_by_index import get_stock_by_idx

stocks = pd.read_csv("data/Stocks.csv")
idx_comp = pd.read_json("data/IndexComposition.json")
stock_idx_names = list(idx_comp)

count = 0
while count < 10:

    test_input = random.choice(stock_idx_names)
    print("Index search: ", test_input)
    get_stock_by_idx(test_input)
    print("\n")
    count += 1