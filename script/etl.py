import pandas as pd
from sqlalchemy import create_engine
import logging
from datetime import datetime

# ------------------- LOGGING SETUP -------------------
logging.basicConfig(
    filename='etl.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ------------------- CONFIG -------------------
CSV_FILE = 'Most Streamed Spotify Songs 2024.csv'

DB_USER = 'postgres'
DB_PASSWORD = '12345'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'spotify_db'
TABLE_NAME = 'songs_table'

# ------------------- EXTRACT -------------------
def extract(csv_file):
    logging.info("Starting data extraction")
    df = pd.read_csv(csv_file)
    logging.info(f"Extracted {len(df)} records")
    return df

# ------------------- TRANSFORM -------------------
def transform(df):
    logging.info("Starting data transformation")

    # Drop duplicates
    df = df.drop_duplicates()

    # Drop rows with missing values
    df = df.dropna()

    # Convert column names to lowercase
    df.columns = [col.lower() for col in df.columns]

    logging.info(f"Transformed data count: {len(df)}")
    return df

# ------------------- LOAD -------------------
def load(df):
    logging.info("Starting data load")

    engine = create_engine(
        f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )

    df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)

    logging.info("Data successfully loaded into PostgreSQL")

# ------------------- MAIN -------------------
def main():
    start_time = datetime.now()
    logging.info("ETL job started")

    try:
        df = extract(CSV_FILE)
        df = transform(df)
        load(df)
        logging.info("ETL job completed successfully")
    except Exception as e:
        logging.error(f"ETL job failed: {e}")

    end_time = datetime.now()
    logging.info(f"ETL duration: {end_time - start_time}")

if __name__ == "__main__":
    main()
