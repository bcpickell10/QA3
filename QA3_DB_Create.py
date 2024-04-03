import sqlite3

# Connect to the database (creates a new database if not exist)
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

# Create Finance table
cursor.execute('''CREATE TABLE Finance (
                Question TEXT PRIMARY KEY,
                Answer_Choices TEXT,
                Answers TEXT)''')

# Create Analytics table
cursor.execute('''CREATE TABLE Analytics (
                Question TEXT PRIMARY KEY,
                Answer_Choices TEXT,
                Answers TEXT)''')

# Create Management table
cursor.execute('''CREATE TABLE Management (
                Question TEXT PRIMARY KEY,
                Answer_Choices TEXT,
                Answers TEXT)''')

# Create Analytic Thinking table
cursor.execute('''CREATE TABLE Analytic_Thinking (
                Question TEXT PRIMARY KEY,
                Answer_Choices TEXT,
                Answers TEXT)''')

# Create Apps Development table
cursor.execute('''CREATE TABLE Apps_Development (
                Question TEXT PRIMARY KEY,
                Answer_Choices TEXT,
                Answers TEXT)''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Tables created successfully.")
