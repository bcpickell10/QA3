import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

def print_table_data(table_name):
    # Retrieve data from the specified table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Print the table header
    print(f"Table: {table_name}\n")
    if len(rows) == 0:
        print("No data available.")
        return

    # Print data row by row
    for row in rows:
        print(row)
    print("\n")

# Print data from each table
tables = ["Finance", "Analytics", "Management", "Analytic_Thinking"]
for table in tables:
    print_table_data(table)

# Close connection
conn.close()
