import pandas as pd

data = {
    'Name': ['Amit', 'Riya', 'Raj'],
    'Marks': [80, 90, 70]
}

df = pd.DataFrame(data)

print(df)
print("Average Marks:", df['Marks'].mean())
print("Highest Marks:", df['Marks'].max())
print("Lowest Marks:", df['Marks'].min())
