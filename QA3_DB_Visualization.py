import sqlite3

def display_table(table_name):
    # Connect to the database
    conn = sqlite3.connect('quiz_database.db')
    cursor = conn.cursor()

    # Retrieve data from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Print table header
    print(f"\nTable: {table_name}\n")
    print("{:<5} {:<100} {:<100}".format("ID", "Question", "Answer"))

    # Print table data
    for row in rows:
        print("{:<5} {:<100} {:<100}".format(row[0], row[1], row[2]))

    # Close connection
    conn.close()

# Display tables
tables = ["Finance", "Analytics", "Management", "Analytic_Thinking", "Apps_Development"]
for table in tables:
    display_table(table)
