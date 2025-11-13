import pandas as pd

url = "data/movies_metadata.csv"
df = pd.read_csv(url)
print(df.head())
print(df.describe())
print(df[["belongs_to_collection", "homepage", "tagline"]]) # Варіант запису 1
df.tagline.fillna("-", inplace=True) # Cтарий варіант
# df.fillna({"tagline":"-"}, inplace=True) #1 Новий варіант
df["tagline"] = df["tagline"].fillna("-") #2 Новий варіант
print(df.tagline)
print(df.homepage)
df["homepage"] = df["homepage"].fillna("no homepage")
print(df.belongs_to_collection)
df.fillna({"belongs_to_collection":"{}"}, inplace=True)
df.info()
df.dropna(inplace=True)
print(df.isnull().sum())
df.info()