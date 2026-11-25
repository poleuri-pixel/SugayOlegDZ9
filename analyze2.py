import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных из JSON
with open("events.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Преобразование данных в DataFrame
df = pd.DataFrame(data["events"])

# Просмотр первых пяти событий
print("Первые 5 событий:")
print(df.head())

# Анализ данных
print("\nВсего событий:", len(df))

print("\nРаспределение событий по типам:")
print(df["signature"].value_counts())

# Визуализация
plt.figure(figsize=(12, 7))

ax = sns.countplot(
    data=df,
    x="signature",
    order=df["signature"].value_counts().index
)
for container in ax.containers:
    ax.bar_label(container, padding=3)
    
plt.title("Распределение типов событий безопасности")
plt.xlabel("Тип события")
plt.ylabel("Количество событий")

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()
