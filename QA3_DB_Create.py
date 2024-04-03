import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('quiz_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create Finance table
cursor.execute('''CREATE TABLE IF NOT EXISTS Finance (
                    Question TEXT PRIMARY KEY,
                    Answer TEXT)''')

# Create Analytics table
cursor.execute('''CREATE TABLE IF NOT EXISTS Analytics (
                    Question TEXT PRIMARY KEY,
                    Answer TEXT)''')

# Create Management table
cursor.execute('''CREATE TABLE IF NOT EXISTS Management (
                    Question TEXT PRIMARY KEY,
                    Answer TEXT)''')

# Create Analytic_Thinking table
cursor.execute('''CREATE TABLE IF NOT EXISTS Analytic_Thinking (
                    Question TEXT PRIMARY KEY,
                    Answer TEXT)''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and tables created successfully!")
