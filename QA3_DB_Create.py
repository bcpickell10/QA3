import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS Finance (
                    Question_ID INTEGER PRIMARY KEY,
                    Question TEXT,
                    Answer TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Analytics (
                    Question_ID INTEGER PRIMARY KEY,
                    Question TEXT,
                    Answer TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Management (
                    Question_ID INTEGER PRIMARY KEY,
                    Question TEXT,
                    Answer TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Analytic_Thinking (
                    Question_ID INTEGER PRIMARY KEY,
                    Question TEXT,
                    Answer TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Apps_Development (
                    Question_ID INTEGER PRIMARY KEY,
                    Question TEXT,
                    Answer TEXT)''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Tables created successfully!")
