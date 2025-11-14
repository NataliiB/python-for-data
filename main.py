import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

url = "data/movies_metadata.csv"
df = pd.read_csv(url)
# print(df.head())
# print(df.describe())
# print(df.info())
# print(df[["belongs_to_collection", "homepage", "tagline"]]) # Варіант запису 1
# df.tagline.fillna("-", inplace=True) # Cтарий варіант
# df.fillna({"tagline":"-"}, inplace=True) #1 Новий варіант
df["tagline"] = df["tagline"].fillna("-") #2 Новий варіант
# print(df.tagline)
# print(df.homepage)
df["homepage"] = df["homepage"].fillna("no homepage")
# print(df.belongs_to_collection)
df.fillna({"belongs_to_collection":"{}"}, inplace=True)
# df.info()
df.dropna(inplace=True)
# print(df.isnull().sum())
# df.info()
# print(df.budget)
# print(df['budget'].sum())
# print(df.columns)
# print(df.iloc[:, 10])
# df.info()
genres_counts = df['genres'].value_counts()
def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return [genre["name"] for genre in genres]
    except:
        pass
df["genres"] = df['genres'].apply(extract_genres)
# print(df.head())
# print(df.genres)
all_genres = df["genres"].explode()
genres_counts = all_genres.value_counts()
# print(genres_counts)
# print(genres_counts.index)
# print(genres_counts.values)
plt.figure(figsize=(10,6))
sns.barplot(x=genres_counts.index, y=genres_counts.values)
plt.title('Chart')
plt.xlabel('genres')
plt.ylabel('counts')
plt.xticks(rotation=60)
plt.show()
