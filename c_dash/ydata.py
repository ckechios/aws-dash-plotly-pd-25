import yfinance as yf

df = yf.download("IBM", 
                 start="2020-01-01", 
                 end="2021-01-01",
                 multi_level_index=False)
print(df.head())
# df.to_csv("IBM.csv")
