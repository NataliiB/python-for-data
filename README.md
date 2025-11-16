# Аналіз даних фільмів

```python
# Імпорт необхідних модулів
import pandas as pd  # робота з табличними даними
import matplotlib.pyplot as plt  # візуалізація даних
import seaborn as sns  # красива візуалізація
import ast  # робота з абстрактним синтаксичним деревом коду

# Завантаження даних
url = "data/movies_metadata.csv"
df = pd.read_csv(url)  # читає CSV у DataFrame

# Попередній огляд даних
print(df.head())      # перші рядки
print(df.describe())  # статистика по числових стовпцях
print(df.info())      # структура таблиці: стовпці, типи даних, ненульові значення

# Робота зі стовпцями
print(df[["belongs_to_collection", "homepage", "tagline"]])  # вивід потрібних колонок
df.tagline.fillna("-", inplace=True)  # заповнення пропущених значень у tagline
df.fillna({"tagline":"-"}, inplace=True)  # альтернативний спосіб
df["tagline"] = df["tagline"].fillna("-")  # ще один варіант
df["homepage"] = df["homepage"].fillna("no homepage")
df.fillna({"belongs_to_collection":"{}"}, inplace=True)
df.dropna(inplace=True)  # видалення рядків з пропущеними значеннями
print(df.isnull().sum())  # перевірка пропущених значень
print(df['budget'].sum())  # сума бюджету

# Аналіз жанрів
genres_counts = df['genres'].value_counts()  # підрахунок кількості кожного жанру

def extract_genres(genre_str):
    try:
        genres = ast.literal_eval(genre_str)  # перетворення рядка у список
        return [genre["name"] for genre in genres]  # повертає список назв жанрів
    except:
        pass

df["genres"] = df['genres'].apply(extract_genres)  # застосування до стовпця
all_genres = df["genres"].explode()  # кожен жанр у окремий рядок
genres_counts = all_genres.value_counts()  # підрахунок частоти жанрів

# Візуалізація жанрів
plt.figure(figsize=(10,6))
sns.barplot(x=genres_counts.index, y=genres_counts.values, palette="viridis")
plt.title('Chart')
plt.xlabel('genres')
plt.ylabel('counts')
plt.xticks(rotation=60)
plt.show()
