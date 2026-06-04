from fetch_news import fetch_news
from transform import transform
from database import connect

def  run_etl():
    print("Fetching news...")
    data = fetch_news()

    print("Transforming data...")
    df = transform(data)

    print("Saving to database...")
    conn = connect()

    df.to_sql("news", conn, if_exists="replace", index=False)

    conn.close()

    print("ETL Completed Successfully!")

run_etl()