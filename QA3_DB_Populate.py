import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

# Define function to insert data into tables
def insert_question_and_answer(question, answer_choices, correct_answer, table_name):
    cursor.execute(f"INSERT INTO Questions (Question) VALUES (?)", (question,))
    question_id = cursor.lastrowid
    for choice in answer_choices:
        cursor.execute(f"INSERT INTO Answer_Choices (Question_ID, Choice) VALUES (?, ?)", (question_id, choice))
    cursor.execute(f"INSERT INTO Answers (Question_ID, Correct_Answer) VALUES (?, ?)", (question_id, correct_answer))

# Questions and answers for Finance
finance_questions = [
    ("What is the primary goal of financial management?", ["a. Maximizing profit", "b. Increasing market share", "c. Reducing costs", "d. Maximizing shareholder wealth"], "d"),
    ("True or False: The Balance Sheet shows the financial position of a company at a specific point in time.", ["True", "False"], "True"),
    ("What does ROI stand for?", ["a. Rate of Investment", "b. Return of Interest", "c. Return on Investment", "d. Revenue of Interest"], "c"),
    ("Which of the following is not a type of financial statement?", ["a. Balance Sheet", "b. Purchase Order", "c. Income Statement", "d. Cash Flow Statement"], "b"),
    ("What is the formula to calculate Net Profit?", ["a. Revenue - Expenses", "b. Revenue / Expenses", "c. Revenue * Expenses", "d. Revenue + Expenses"], "a"),
    ("Which financial statement reports a company's revenues and expenses?", ["a. Balance Sheet", "b. Income Statement", "c. Cash Flow Statement", "d. Statement of Retained Earnings"], "b"),
    ("What is the term for the process of spreading out investments to reduce risk?", ["a. Consolidation", "b. Accumulation", "c. Diversification", "d. Aggregation"], "c"),
    ("What is the abbreviation for the Federal Reserve System in the United States?", ["a. Fed", "b. IRS", "c. SEC", "d. FASB"], "a"),
    ("Which financial ratio measures a company's ability to pay its short-term debts?", ["a. Debt to Equity Ratio", "b. Current Ratio", "c. Return on Equity", "d. Inventory Turnover Ratio"], "b"),
    ("True or False: Depreciation is a non-cash expense.", ["True", "False"], "True")
]

# Questions and answers for Analytics
analytics_questions = [
    ("What is data analytics?", ["a. The science of analyzing raw data to make conclusions about that information", "b. The process of creating data", "c. Storing data in databases", "d. Sharing data online"], "a"),
    ("True or False: Descriptive analytics deals with analyzing data to identify patterns and trends.", ["True", "False"], "True"),
    ("What is the primary goal of predictive analytics?", ["a. Understand the past", "b. Analyze the present", "c. Predict future outcomes based on historical data", "d. None of the above"], "c"),
    ("Which of the following is a commonly used data visualization tool?", ["a. Microsoft Excel", "b. Tableau", "c. MATLAB", "d. SPSS"], "b"),
    ("What is the process of cleaning and preparing data for analysis called?", ["a. Data Wrangling", "b. Data Analysis", "c. Data Visualization", "d. Data Mining"], "a"),
    ("True or False: Correlation implies causation.", ["True", "False"], "False"),
    ("What statistical measure describes the spread of data around the mean?", ["a. Mean", "b. Standard Deviation", "c. Median", "d. Mode"], "b"),
    ("What does KPI stand for?", ["a. Key Personal Indicator", "b. Key Performance Indicator", "c. Key Productivity Index", "d. Key Projected Indicator"], "b"),
    ("Which machine learning technique is used for classification problems?", ["a. Linear Regression", "b. Logistic Regression", "c. Decision Trees", "d. K-Means Clustering"], "b"),
    ("What is the process of discovering hidden patterns in large datasets called?", ["a. Data Mining", "b. Data Analysis", "c. Data Wrangling", "d. Data Visualization"], "a")
]

# Questions and answers for Management
management_questions = [
    ("What is management?", ["a. The process of leading people", "b. The process of controlling resources", "c. The process of planning, organizing, leading, and controlling resources to achieve specific goals", "d. The process of making decisions"], "c"),
    ("True or False: Management is only applicable in business settings.", ["True", "False"], "False"),
    ("What does SWOT analysis stand for?", ["a. Strengths, Weaknesses, Opportunities, Threats", "b. Sales, Workforce, Operations, Technology", "c. Strategy, Work, Operations, Trends", "d. None of the above"], "a"),
    ("Which management theory emphasizes the importance of understanding employee needs?", ["a. Scientific Management", "b. Administrative Management", "c. Bureaucratic Management", "d. Maslow's Hierarchy of Needs"], "d"),
    ("What is the process of setting goals and determining the best way to achieve them?", ["a. Controlling", "b. Organizing", "c. Planning", "d. Leading"], "c"),
    ("True or False: Leadership and management are interchangeable terms.", ["True", "False"], "False"),
    ("What is the term for the formal system of tasks and reporting relationships?", ["a. Organizational Behavior", "b. Organizational Culture", "c. Organizational Structure", "d. Organizational Change"], "c"),
    ("What type of power comes from one's position within an organization?", ["a. Legitimate Power", "b. Reward Power", "c. Expert Power", "d. Referent Power"], "a"),
    ("What is the term for a situation where two or more people work together to achieve a common goal?", ["a. Conflict", "b. Collaboration", "c. Competition", "d. Cooperation"], "b"),
    ("What is the process of monitoring performance and making adjustments as needed?", ["a. Leading", "b. Planning", "c. Organizing", "d. Controlling"], "d")
]

# Questions and answers for Analytic_Thinking
analytic_thinking_questions = [
    ("What is critical thinking?", ["a. The subjective analysis of an issue", "b. The objective analysis and evaluation of an issue in order to form a judgment", "c. The emotional reaction to a situation", "d. The acceptance of information at face value"], "b"),
    ("True or False: Analytical thinking is synonymous with creative thinking.", ["True", "False"], "False"),
    ("What is the first step in the problem-solving process?", ["a. Implementing the solution", "b. Generating alternatives", "c. Identifying the problem", "d. Evaluating the results"], "c"),
    ("Which of the following is a common problem-solving technique?", ["a. Root Cause Analysis", "b. Assumption", "c. Conformation Bias", "d. Stigmatization"], "a"),
    ("What is the process of examining assumptions and evidence to form logical conclusions?", ["a. Reasoning", "b. Emotion", "c. Intuition", "d. Creativity"], "a"),
    ("True or False: Analytical thinking requires one to accept information at face value.", ["True", "False"], "False"),
    ("What is the term for breaking down a complex problem into smaller, manageable parts?", ["a. Assumption", "b. Intuition", "c. Decomposition", "d. Imagination"], "c"),
    ("What is the process of generating multiple solutions to a problem?", ["a. Reasoning", "b. Imagination", "c. Intuition", "d. Brainstorming"], "d"),
    ("True or False: Critical thinking involves only questioning others' ideas.", ["True", "False"], "False"),
    ("What is the term for the ability to see situations from multiple perspectives?", ["a. Perspective Taking", "b. Tunnel Vision", "c. Biased Perspective", "d. Narrow-mindedness"], "a")
]

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Questions (
                    Question_ID INTEGER PRIMARY KEY,
                    Question TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Answer_Choices (
                    Choice_ID INTEGER PRIMARY KEY,
                    Question_ID INTEGER,
                    Choice TEXT,
                    FOREIGN KEY(Question_ID) REFERENCES Questions(Question_ID))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Answers (
                    Answer_ID INTEGER PRIMARY KEY,
                    Question_ID INTEGER,
                    Correct_Answer TEXT,
                    FOREIGN KEY(Question_ID) REFERENCES Questions(Question_ID))''')

# Insert data into tables
for question, choices, correct_answer in finance_questions:
    insert_question_and_answer(question, choices, correct_answer, "Finance")

for question, choices, correct_answer in analytics_questions:
    insert_question_and_answer(question, choices, correct_answer, "Analytics")

for question, choices, correct_answer in management_questions:
    insert_question_and_answer(question, choices, correct_answer, "Management")

for question, choices, correct_answer in analytic_thinking_questions:
    insert_question_and_answer(question, choices, correct_answer, "Analytic_Thinking")

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully!")
