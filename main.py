import pandas as pd

# задание 1
df = pd.read_csv("data.csv")

df["Date"] = pd.to_datetime(df["Date"])

df.rename(columns={"Temp": "Value"}, inplace=True)

values = df["Value"]

print("Количество значений:", len(values))
print(values.head()) # первые 5
# print(values)