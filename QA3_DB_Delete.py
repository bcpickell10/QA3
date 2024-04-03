import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

# Define function to delete all data from tables
def delete_data_from_table(table_name):
    cursor.execute(f"DELETE FROM {table_name}")

# Tables to delete data from
tables = ["Finance", "Analytics", "Management", "Analytic_Thinking"]

# Delete data from each table
for table in tables:
    delete_data_from_table(table)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data deleted successfully!")
