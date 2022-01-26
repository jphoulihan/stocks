import pandas as pd
import numpy as np
from utils.check_list_item_len import all_equal

stocks = pd.read_csv("data/Stocks.csv")
idx_comp = pd.read_json("data/IndexComposition.json")

# are all stocks in json file from sedol1 col, are they all valid identifiers ?

# Unique Identifiers
# sedol1 7 chars, some are of length 6
# cusip 9 chars, some cusips appear shorter in Stocks.csv
# isin 12 chars

# Some CUSIPS have same values of SEDOL1 in csv file

stock_idx_names = list(idx_comp)
temp_arr = []

for i in range(len(stock_idx_names)):
    list_arr = idx_comp[stock_idx_names[i]][0]
    temp_arr.append(list_arr)

flat_list = [i for sub in temp_arr for i in sub]
num_arr = np.array(flat_list)

len_check = np.vectorize(len)
arr_len = len_check(num_arr)

error_idx_list = []
for i in range(len(arr_len)):
    if arr_len[i] != 7:
        error_idx_list.append(arr_len[i])

print(
    "Are all elements of error_idx_list of same length?", all_equal(error_idx_list), '\n'
)  # are all elements in list of same length?

idx_for_flat_list = np.where(arr_len == 6)
ls = np.asarray(idx_for_flat_list)
id_check = ls[0].tolist()

id_err_list = []
for i in id_check:
    id_err_list.append(flat_list[i])

print("List of stock identifiers of length 6:", id_err_list, '\n')

# are all elements of error list in ID_CUPID, rows of filtered df should be equal in length to id_err_list
cusip_df = stocks[stocks["ID_CUSIP"].isin(id_err_list)]

if len(cusip_df) == len(id_err_list):
    print("All IDs of character length 7 found in Stocks.csv")
else:
    print(str(len(id_err_list) - len(cusip_df)),'of',str(len(id_err_list)), "CUSIP IDs not returned in Stocks.csv, May indicate duplicate IDs")

print(cusip_df)
print('\n')

clean_list = flat_list.copy()

for i in id_err_list:
    clean_list.remove(
        i
    )  # list of valid stock ids from json file, but cusips seem to contian ids of len 6!

sedol1_df = stocks[stocks["ID_SEDOL1"].isin(clean_list)]

if len(clean_list) == len(sedol1_df):
    print("All IDs of character length 7 found in Stocks.csv")
else:
    print(str(len(clean_list) - len(sedol1_df)), "SEDOL1 IDs not returned in Stocks.csv, May indicate duplicate IDs\n")

flat_set = set(flat_list)
id_err_set = set(id_err_list)
clean_set = set(clean_list)

print('Duplicates found from each list:\n')
print(str(len(id_err_list) - len(id_err_set)), 'id_err_list')
print(str(len(clean_list) - len(clean_set)), 'clean_list')
print(str(len(flat_list) - len(flat_set)), 'total duplicates of combined lists\n' )

print(id_err_set)

cusip_set_df = stocks[stocks["ID_CUSIP"].isin(id_err_set)]
sedol1_set_df = stocks[stocks["ID_SEDOL1"].isin(id_err_set)]

print(cusip_df)
print(sedol1_set_df) #sedol yields results for each 6 digit id from set

sedol1_flatset_df = stocks[stocks["ID_SEDOL1"].isin(flat_set)]


print(len(flat_list))
print(len(flat_set)) 

print(sedol1_flatset_df) #row count should == flat_set length if isin() ignores duplicates

