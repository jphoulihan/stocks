import pandas as pd

stocks = pd.read_csv("data/Stocks.csv")


# this function is reused in another file, the second parameter is a boolean allowing reuse without exporting the results
def get_stock_json(id, export_file):
    if id is None or not isinstance(id, str):
        print("Please enter a valid stock identifier, input must be of type string")
        return 

    res = stocks[
        (stocks["ticker"] == id)
        | (stocks["ID_CUSIP"] == id)
        | (stocks["ID_ISIN"] == id)
        | (stocks["ID_SEDOL1"] == id)
    ]

    if res.empty:
        print("The stock identifier entered was not found in Stocks.csv, please enter a valid stock identifier")
        return
    elif export_file is True:
        name = res.iloc[0]["ticker"]
        file_name = name.replace(" ", "_").lower()
        res.iloc[0].to_json(
            f"exports/stock/{file_name}.json", orient="index", indent=2
        )
        print('File exported')
        return
    else:
        return res.iloc[0].to_json(orient="index", indent=2)
