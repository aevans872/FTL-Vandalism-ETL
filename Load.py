import sqlite3

def load_data(df, db_path):
    # Create a new database
    conn = sqlite3.connect("vandalism.db")
    # Make case_id column the index and primary key
    df.set_index('case_id', inplace=True)
    # Write df to database table
    df.to_sql('vandalism', conn, if_exists='replace')
    # Close the connection
    conn.close()