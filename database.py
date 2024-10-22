import duckdb
import pandas as pd

# Connect to DuckDB (or create it if it doesn't exist)
def connect_db(db_name='company_data.db'):
    return duckdb.connect(db_name)

# Create tables for storing company data
def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS company_overview (
        company TEXT,
        overview TEXT
    );
    """)
    
    conn.execute("""
    CREATE TABLE IF NOT EXISTS company_finances (
        company TEXT,
        year TEXT,
        revenue TEXT,
        profit TEXT
    );
    """)

# Insert company overview data
def insert_overview(conn, company, overview):
    conn.execute("INSERT INTO company_overview (company, overview) VALUES (?, ?)", [company, overview])

# Insert financial data (expects a pandas DataFrame)
def insert_financials(conn, financial_data):
    for _, row in financial_data.iterrows():
        conn.execute("INSERT INTO company_finances (company, year, revenue, profit) VALUES (?, ?, ?, ?)",
                     [row['company'], row['Year'], row['Revenue'], row['Profit']])

# Fetch all data from a specified table
def fetch_all_data(conn, table_name):
    return conn.execute(f"SELECT * FROM {table_name}").fetchdf()

# Close the DuckDB connection
def close_db(conn):
    conn.close()
