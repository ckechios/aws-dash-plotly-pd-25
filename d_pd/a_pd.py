import pandas as pd 
import matplotlib.pyplot as plt

stocks = pd.read_csv('data_analysis.csv')

"""
print(stocks.head())
print(stocks.tail())
print(stocks.describe())
# Look at the data types - strings are imported as objects
print(stocks.dtypes)
"""

# Replace the $ symbol
print(stocks.head())
stocks = stocks.replace({'\$':''}, regex = True)
stocks.head()


# How to duplicate a column?
# 
# Copy Quantity-of-Stocks to a new column
stocks["q2"] = stocks["Quantity of stocks"]
print(stocks.head())

# How to duplicate a column?
# 
# Copy Quantity-of-Stocks to a new column
stocks["q2"] = stocks["Quantity of stocks"]
print(stocks.head())

# Removing all spaces with - only for the column header
stocks.columns = stocks.columns.str.replace(" ", "-")
# This line below wont work as we are only replacing the columns not the entire data set
stocks.columns = stocks.columns.str.replace(",", "*")
print(stocks.head())

# However all the following will work
print("Replace character in contents of a particular column")
stocks['Quantity-of-stocks'] = stocks['Quantity-of-stocks'].str.replace(",", "-")
print(stocks.head())

# Replace , with null
print("Replace all commas with nothing")
stocks = stocks.replace(",","", regex = True)
print(stocks.head())

# now remove the -
print("Replace all dashes with nothing")
stocks = stocks.replace("-","", regex = True)
print(stocks.head())

# Delete column q2, but this wont persist the deletion, show this before showing inplace
print("Remove column q2")
stocks.drop('q2',axis=1)
print(stocks.head())

# Q2 confirm drop
print("^^^^^ q2 not dropped. Now will be dropped")
stocks.drop('q2',axis=1,inplace=True)
print(stocks.head())

# assign stocks to dataframe
df = stocks
print(df.head())

# Renaming column names
print("Rename columns")
df.columns = ['ID', 'Desk', 'Stock', 'Qty', 'Price', 'Position']
print(df.head())

# Renaming a particular column
# Following command will show the new column name, but will not persist it
print("Rename one column")
df = df.rename(columns = {'Desk':'The Desk'})
print(df.head())

# Renaming The Desk back to Desk
print("Rename The Desk back to Desk")
df = df.rename(columns = {'The Desk':'Desk'})
print(df.head())

# Cast data types Show all the data types before casting them
print(df.dtypes)

# Converting data types
df = df.astype({"ID": int, "Desk": str, "Stock": str, "Qty": int, "Price": float, "Position": str}) 
print(df.dtypes)

# Backing up df to dfcopy
print("----- Copying dataframes -----")
dfcopy = df.copy()
# Also creating a copy of df in df2, both seem to do the same thing
df2 = df
print("DF2",df2.head())
print("DFCOPY",dfcopy.head())

print("Types for both")
# Printing data types for both
print(df.dtypes)
print(dfcopy.dtypes)

# Run this to show how df2 is an instance of df, changing df will affect df2
# This will change both df and df2
print("Effect of changing df on df2 and dfcopy")
df.Position = 0
print(df2.head())
print(dfcopy.head())
print("Changing df changes df2 not dfcopy")

# Restoring df back to what it was - show later
print("\n---- Restoring df")
df = dfcopy.copy()

### Learn how copying creates a new space in memory for df

# This creates a new df which is different from df2, hence df2 now does not reflect the new values of df

# Shows copy only changes df not df2
print(df.head())
print(df2.head())
print(dfcopy.head())
print("df changes, but df2 still remains the same.")

# To prove that df and df2 are separate if we change Position of df df2 does not change
# This will change both df and df2
print("Double check that df is separate from df2 and dfcopy. Setting position to 5 for df")
df.Position = 5
print(df.head())
print(df2.head())
print(dfcopy.head())

# Restoring df back to what it was
print("\n---- Restoring df again")
df = dfcopy.copy()

# Another way of replacing
print("Another way of replacing values: BUY/SELL to 0/1")
df=df.replace(to_replace="BUY",value=0)
df=df.replace(to_replace="SELL",value=1)
print(df.head())
print(dfcopy.head())

# Restore df back to original
df = dfcopy.copy()
print(df.head())

# Making sure that df has the same datatypes
print("Check data types\n",df.dtypes)
print("Check data types\n",dfcopy.dtypes)

print("Describing ----------------")
print(df.describe())
print("Describing -- include floats --------------")
print(df.describe(include = "float"))
print("Describing -- include objects --------------")
print(df.describe(include = "object"))
print("Describing -- include Float and object only  --------------")
print(df.describe(include = ["float","object"]))
# because objects are string values there is no mean, std,min or unque, top, freq
print("\nUsing exclude:")
print(df.describe(exclude = "int"))
print("\Different percentiles:")
print(df.describe(percentiles = [0.1, 0.4, 0.9]))

### Learn how to query a data frame
# Price < 100
print(f"\n {'-'*5} Querying data frame Price < 100")
priceunderhundred = df.Price < 100
underhundred = df.loc[priceunderhundred] 
# dir(underhundred)
print(underhundred.head())
# underhundred.count()
# underhundred.ID.count()

print("Sort by ID:")
print(df.sort_values('ID'))
# underhundred.sort_values('ID')

# Price under 300 and Qty is greater than 500
priceCondition = df.Price > 100
mask_Qty = df.Qty > 500
priceAbove100_qtyAbove500 = df.loc[priceCondition & mask_Qty]
print("SHowing only price > 100 and qty>500")
print(priceAbove100_qtyAbove500.head())

# price under 100 and position is buy
priceunderhundred = df.Price < 100
mask_Position = df.Position == "BUY"
price_lessthan100_positionBuy = df.loc[priceunderhundred & mask_Position]
print("SHowing only price < 100 and position == Buy")
print(price_lessthan100_positionBuy.head())


# Count the number of row
print("-"*20,"Count")
print(df.count())
print("-"*20)
# ---- Print the total rows in data frame ----
print("Shape",df.shape[0])
print(len(df))
print(df.count()["Price"])
print("-"*20)
# Print all the above counts
print("          Total Count:",df.__len__())
print("          Price < 100:",len(underhundred))
print("Price>100 and Qty>500:",len(priceAbove100_qtyAbove500))
print("    Price>100 and BUY:",price_lessthan100_positionBuy.shape[0])


"""
### Learn how to Add a new Column that shows the total value of a trade

For this we need to understand Lambda

### Explain how a lambda works
lambda is the keyword
param is the parameter received by lambda

(lambda param: function)(param)
Eg. (lambda x: x+2)(5)
"""

# (lambda param: function)(param)

print("-"*20,"\n")
print("       add 2:",(lambda x: x+2)(3))
print("  power of 2:",(lambda x: x**2)(4))
print("with 2 param:",(lambda x,y: (x**2)+y)(4,5))

def add(x,y):
    return x+y

print("with fn call:",(lambda x,y: add(x,y))(4,5))
print(f"{'-'*20} ****** {'-'*20}")
"""
### Learn how to Value a trade
 
Total Value = Qty * Price

1. We will do this by creating a function called value calulation
2. Use df.apply() to Apply the function to the data frame using a lambda

using df.apply(passing a lambda, axis=1)

.apply() is an alternative looping over a DataFrame.

axis = 1 means columns, add the new value as a column
"""
df.head(2).apply(lambda x: print(x), axis="columns")
print("--------------------------------------------")
df.head(2).apply(lambda x: print(x), axis=1)


# Add a new Value column to df setting value to 
#     positive if its a buy, 
#     negative if its a sell
print("------- Add a new column with value calculation ------")
def value_calculation(row):
    value = row["Qty"] * row["Price"]
    if row["Position"] == "SELL":
        value = value * (-1)
    return value

# Another way of doing the above without a function, 
# df.apply(lambda row: (row["Qty"] * row["Price"]) if True else (row["Qty"] * row["Price"] * -1),axis=1)

df.apply(lambda row: value_calculation(row), axis=1)
# add as a new column 
df["newcolumn"] = df.apply(lambda row: value_calculation(row), axis=1)
print(df.head())

# Renaming the column 'newcolumn' to PositionNumeric
# To persisit the above add inplace = True
print("------- Renamed newcolumn to Value ------")
df.rename(columns={'newcolumn':'Value'}, inplace=True)
print(df.head(2))

"""
### Learn how to Calculate breach level
Option 1 with def:

OPtion 2 inline function 
"""
# risk limit = 10,000,000
# Example of absolute function
n=-232.23
print(f"Value of n:{n} using abs(n): {abs(n)}")

"""
    Add a new Risk Limit Breached column to see if value 
    is greater than Risk Limit
    
"""

print("------- Breach Level Check ------")
riskLimit=10000000
def risk_breach_check(row, limitOfRisk):
    if abs(row["Value"]) > limitOfRisk:
        return ("Yes")
    else:
#         return ("No"+str(limitOfRisk)+" * "+str(row["Value"])+ " * "+str(row["ID"]))
        return "No"

df.apply(lambda row: risk_breach_check(row,riskLimit), axis=1)
# add as a new column 
df["Risk-breach"] = df.apply(lambda row: risk_breach_check(row,riskLimit), axis=1)

print(df.head())

"""
### Learn how Ternary operator works

x if C else y

Create a new column called RiskLim2 to show the above and below yield the same output

"""
df["RLmt2"] = df.apply(lambda row: ("Yes") if (abs(row["Value"]) > riskLimit) else ("No"),axis=1)
print("--------- Check Limit sorted by ID -------")
print(df.sort_values("ID").head())

df = df.drop("RLmt2", axis="columns")
# or df.drop("RLmt2", axis=1)   #same as above
print("--------- Dropped RLmt2 column -------")
print(df.head())

"""
### For Instructors only
#### Creating a pandas data frame

data = {'First Column Name':  ['First value', 'Second value',...],
        'Second Column Name': ['First value', 'Second value',...],
         ....
        }

df = pd.DataFrame (data, columns = ['First Column Name','Second Column Name',...])

print (df)

### Learn how to create Pandas data frame without importing CSV like above

Use the new data to create a Pandas data frame called comdf for Commission Data Frame

"""

"""
    Create a new dataframe with columns Desk and Commission, with values
    EA=0.03%
    UKS=0.04%
    US=0.05%
"""

# Declare a dictionary data type with column names and row values
data = { "Desk" : ["EA","UKS","US"],
         "Commission" : [0.03,0.04,0.05]
       }

comdf = pd.DataFrame (data, columns=["Desk","Commission"])
# print(type(data))
print(comdf)

print("different ways of gettting percentage values")
# Three ways of getting the percentage value for a particular Desk
# 1 - query method
# df.query(Row==cond)[Column].values
print("Option 1:",comdf.query('Desk=="EA"')["Commission"].values)
# 2 df[row with df[] condition][column to pull].values
commValue=comdf[comdf["Desk"]=="EA"]["Commission"].values[0]
print("Option 2:",commValue)
# print(commValue[0])
# 3
# df[col][df[row] == cond].values[0] or iloc[0]
print("Option 3:",comdf["Commission"][comdf["Desk"] == "EA"].iloc[0])

# Backup again at this spot
dfcopy2 = df.copy()

"""
  https://datacarpentry.org/python-ecology-lesson/05-merging-data/index.html

  #### Learn how to perform a Left Join

  A left join will return all of the rows from the left DataFrame, even those rows whose join key(s) do not have values in the right DataFrame. Rows in the left DataFrame that are missing values for the join key(s) in the right DataFrame will simply have null (i.e., NaN or None) values for those columns in the resulting joined DataFrame.

    Find out the comm on each row of df based on the Desk
    
"""
merge_left = pd.merge(left=df, right=comdf, how='left', left_on="Desk", right_on="Desk" )
merge_left.sort_values("ID")
print(merge_left)
print("-"*20)
# The above can be achieved using a different pattern on the dataframe itself
# Same as above
df = df.merge(comdf, how="left", left_on="Desk", right_on="Desk")
# df.sort_values("ID")
print(df.head())
df.rename(columns = {'Commission':'Comm-percentage'}, inplace=True)
print(df.head())

"""
### Learn how to Make another column with the commission values

Hint: 

1. It does not have any complex checks, its a simple calculation
2. Refer to earlier cell where we set Position to 5
"""
df["CommValues"] = abs(df["Value"] * (df["Comm-percentage"]/100))
print("----------- With commission values -----")
print(df.head())

### Learn to Find unique Stock Names in dataset

# Calculate total number of Trades based on the Stock Name
#List unique values in the df['Stock'] column
print(df.Stock.unique())
# or
print("-"*20)
stocklist = df["Stock"].unique()
print(stocklist)
# print(stocklist.dtype)


### Learn to Count total Number of Trade for each type of stock

# Hint:Below how to count, get values

# # This prints all columns
# print(df.loc[df.Stock == "RACE"])
# # Print specific columns
print(df.loc[df.Stock == "RACE",["ID","Desk","CommValues"]])
print("-"*20)
# Print the Commission Values only
print(df.loc[df.Stock == "RACE"].CommValues)
print("-"*20)
print("Count: ", df.loc[df.Stock == "RACE"].__len__())
commissionValues = df.loc[df.Stock == "RACE",["CommValues"]]
print("*"*20)
print(commissionValues)
print("Total Commission Value",commissionValues.sum())
# print(df.loc)

# Learn to Count total Number of Trade for each type of stock

# Iterate through the stocklist and then print the Count
print("Count of each Stock")
totCount = 0
spacetoadd = len("Total Count")
for i in stocklist:
#     print(i)
    print(i.rjust(spacetoadd)+":", df.loc[df.Stock == i].__len__())
    totCount = totCount + df.loc[df.Stock == i].__len__()
print("-"*15)
print("Total Count:",totCount)

# Iterate through the stocklist and then print the Total Value
# ------ Total value of trades -----
print("-"*30)
# TotalValueOfTradesForAStockDf = df.loc[df.Stock == "RACE",["Value"]]
# sumOfStock = TotalValueOfTradesForAStockDf.sum()
# print("SumVal:",sumOfStock[0])
# Showing how to combine all the calculation in one place
print("Total Value of Stocks for the stock:",df.loc[df.Stock == "RACE",["Value","CommValues"]].sum()[0])
print("Total Commission values:",df.loc[df.Stock == "RACE",["Value","CommValues"]].sum()[1])
print("Count:",df.loc[df.Stock == "RACE"].count()[0])
ValSumStock = df.loc[df.Stock == "RACE",["Value","CommValues"]].sum()[0]
TotComm = df.loc[df.Stock == "RACE",["Value","CommValues"]].sum()[1]
print("Value of Stocks, formatted: $"+format(ValSumStock, ",.2f"))
print("Total Value of Stocks: ${0:,.2f} ** Total Commission: ${1:,.2f}".format(ValSumStock,TotComm))

"""
### Learn How formatting works
print("{0:,.2f} ** {1:,.2f}".format(ValSumStock,TotComm))
0 & 1 - is the index numbers of values being sent to the format function
:
the type of formatting we want is passed after the :
In this above case we want commas and 2 decimal places
"""
print("{0:,.2f} ** {1:,.2f}".format(123,23.23445))
print("{0} is worth ${1:,.2f}".format("AMZN",234.45454))


# Formatted printing Eg.
message = 'Hi'
fill = ' '
align = '<'
width = 6
pthis = f'{message:{fill}{align}{width}}'
print(pthis,"Yo")

print(df.head(4))
# df.plot(x='ID', y='Price')
# df.show()
# data=data.astype(float)
plt.plot(df['Value'], 'y', label = "Value label")
plt.legend(loc="upper right")
plt.title('Value Title')
plt.show()
# plt.savefig('grf.jpg')

# df.plot(x='Date', y='Close', rot=90)
# df.plot(x='Date', y='Close', rot=90, title="AMZN Stock Price")
"""
* Line
* Bar
* Pie
* Scatter
* Histogram
"""
# df.plot(x='Date', y='Close', kind='scatter', rot=90, title="AMZN Stock Price")