import pandas as pd

def transform(data):
    df = df[["title", "by", "time", "score", "url"]]
    df.columns = ["title" , "author", "timestamp", "score", "url"]

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    
    df = df.dropna()

    return df