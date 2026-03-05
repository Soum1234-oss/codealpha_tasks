import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("quotes_dataset.csv")

print(df.head())
print(df.info())
print(df.describe())

author_counts = df["Author"].value_counts()

print(author_counts)

author_counts.plot(kind="bar")

plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.title("Quotes per Author")

plt.show()