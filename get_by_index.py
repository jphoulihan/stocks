import json
import pandas as pd
from get_by_id import get_stock_json

stocks = pd.read_csv("data/Stocks.csv")
idx_comp = pd.read_json("data/IndexComposition.json")

stocks.drop_duplicates(subset=None, inplace=True)


def get_stock_by_idx(idx):

    stock_idx_names = list(idx_comp)

    if idx not in stock_idx_names:
        print("Index Composition not found in json file")
        return

    stock_list = idx_comp[idx][0]

    cap_list = []
    set(stock_list)
        
    for i in stock_list:
        json_obj = json.loads(get_stock_json(i, False))
        cap_list.append(json_obj["Market Cap"])

    filtered_cap_list = list(filter(None, cap_list))
    map(float, filtered_cap_list)
    total_cap = sum(filtered_cap_list)

    export = {"Index": idx, "TotalMarketCap": total_cap}
    json_obj = json.dumps(export, indent=4)
    with open(f"exports/market_cap/{idx}.json", "w") as outfile:
        outfile.write(json_obj)
    
    print('File exported')
