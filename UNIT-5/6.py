import pandas as pd

data = {
    'Name': ['Amit', 'Riya', 'Raj'],
    'Marks': [80, 90, 70]
}

df = pd.DataFrame(data)
df.to_csv("student.csv", index=False)

df1 = pd.read_csv("student.csv")
print(df1)
