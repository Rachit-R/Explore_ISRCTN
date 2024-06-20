import sqlite3
from queries import run_all_queries

def main():
    # Path to SQLite database
    db_path = 'isrctn_data.db'

    # Connect to  SQLite database
    conn = sqlite3.connect(db_path)

    # Run all queries; save results to CSV files
    run_all_queries(conn)

    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
