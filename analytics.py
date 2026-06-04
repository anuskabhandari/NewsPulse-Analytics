import pandas as pd
import matplotlib.pyplot as plt
from database import connect

conn = connect()
df = pd.read_sql("SELECT * FROM news", conn)

print(df.head())

# Top authors
top_authors = df["author"].value_counts().head(10)

plt.figure(figsize=(10,5))
plt.bar(top_authors.index, top_authors.values)
plt.title("Top News Authors")
plt.xticks(rotation=45)
plt.show()