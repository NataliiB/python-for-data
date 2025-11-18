import pandas as pd

months = ['jan','feb','mar','apr']
sales  = {
          'revenue': [100,200,300,400],
          'items_sold': [23,43,54,65],
          'new_clients': [10,20,30,40]
          }
sales1 = ['100',"200",'300','400']
df = pd.DataFrame(data=sales, index=months)
data = pd.Series(data=sales1, index=months )
# print(data)
# print(df['revenue'])
# print(df.info())
# print(df.shape)
# print(df.dtypes)
df.revenue = pd.to_numeric(df.revenue, errors='coerce')
# print(df.revenue.dtypes)
# print(df.loc[['feb','apr']])
movies_df = pd.read_csv('data/movies_metadata.csv')
# print(movies_df.to_string())
pd.options.display.max_rows = 10
print(pd.options.display.max_rows)