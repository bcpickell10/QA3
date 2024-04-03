import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

# Function to delete all tables
def delete_all_tables():
    # List all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Drop each table
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")
        print(f"Dropped table: {table[0]}")

# Call the function to delete all tables
delete_all_tables()

# Commit changes and close connection
conn.commit()
conn.close()
