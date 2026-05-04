import pandas as pd

# задание 1
df = pd.read_csv("data.csv")

df["Date"] = pd.to_datetime(df["Date"])

df.rename(columns={"Temp": "Value"}, inplace=True)

values = df["Value"]

# получение сводной информации
print("\n--- Сводная информация о данных ---")

print("\nОбщая информация:")
print(df.info())

print("\nСтатистика:")
print(df.describe())

print("Количество значений:", len(values))
print(values.head()) # первые 5
# print(values)