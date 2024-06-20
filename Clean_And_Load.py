import sqlite3
import pandas as pd

def clean_and_load_csv_to_sqlite(db_path, csv_path):
    # Connect to SQLite database
    conn = sqlite3.connect(db_path)

    # Load CSV data with low_memory set to False to handle dtype warnings
    df = pd.read_csv(csv_path, low_memory=False)

    # Clean column names: remove parentheses ()
    df.columns = [col.replace('(', '').replace(')', '') for col in df.columns]

    # Replace spaces with underscores in column names
    df.columns = [col.replace(' ', '_') for col in df.columns]

    # Save cleaned data back to SQLite
    df.to_sql('ISRCTN', conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    clean_and_load_csv_to_sqlite('isrctn_data.db', 'isrctn_data.csv')
