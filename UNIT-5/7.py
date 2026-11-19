import pandas as pd

data = {
    'Name': ['Amit', 'Riya', 'Raj'],
    'Marks': [80, None, 70]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("After fillna:")
print(df.fillna(0))

print("After dropna:")
print(df.dropna())
