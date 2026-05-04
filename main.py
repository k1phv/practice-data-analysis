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


# задание 2

print("\n--- Очистка данных ---")

before = len(df)

Q1 = df["Value"].quantile(0.25)
Q3 = df["Value"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Нижняя граница:", lower_bound)
print("Верхняя граница:", upper_bound)

df = df[(df["Value"] >= lower_bound) & (df["Value"] <= upper_bound)]

after = len(df)

print("Количество до очистки:", before)
print("Количество после очистки:", after)
print("Удалено значений:", before - after)