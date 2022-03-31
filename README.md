
# **Automating Stock Analysis**

### **Tech Used**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## **Given the two files: Stocks.csv, IndexComposition.json :**
<br>

* ### Create a function that will export all the information for an     individual stock as a .json file when passed any stock identifier: ticker, ID_CUSIP, ID_ISIN, ID_SEDOL1.

<br>

* ### Create a function that takes in an Index identifier: AEX, AMX, AS25, NKY, SPY, etc., and returns
	*   <em>a list of the stocks on that index</em>
	*   <em>the total market capitalization of that index as a .json file.</em>
    
    <br>

* ### Create a function that takes in a date range and a returns a .csv containing the ticker and Next Dividend for all stocks with Next Dividend within that range.

## Additional Info on Identifiers

### SEDOL
Have seven characters, split into two parts: the first six characters are an alphanumeric code, and the seventh character is a trailing check digit. Within the alphanumeric part, letters from B to Z are allowed while numbers from 0 to 9 are allowed as numerals.

SEDOL codes that were issued before January 2004 were strictly composed of numeric characters.

### CUSIP 
A unique identification number assigned to stocks and registered bonds in the United States and Canada. It comprises nine letters and includes letters and numbers.