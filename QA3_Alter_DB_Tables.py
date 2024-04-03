import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

# Define function to add a new column to tables
def add_column_to_table(table_name, column_name):
    cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} TEXT")

# Tables to add the new column to
tables = ["Finance", "Analytics", "Management", "Analytic_Thinking"]

# Add the new column to each table
for table in tables:
    add_column_to_table(table, "Answer_Choices")

# Commit changes and close connection
conn.commit()
conn.close()

print("New column added successfully!")
