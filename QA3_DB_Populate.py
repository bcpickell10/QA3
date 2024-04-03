import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

# Define function to insert data into tables
def insert_data(table_name, questions_and_answers):
    for question, answer in questions_and_answers.items():
        cursor.execute(f"INSERT INTO {table_name} (Question, Answer) VALUES (?, ?)", (question, answer))

# Questions and answers for Finance
finance_questions = {
    "What is the primary goal of financial management?": "d. Maximizing shareholder wealth",
    "True or False: The Balance Sheet shows the financial position of a company at a specific point in time.": "True",
    "What does ROI stand for?": "c. Return on Investment",
    "Which of the following is not a type of financial statement?": "b. Purchase Order",
    "What is the formula to calculate Net Profit?": "a. Revenue - Expenses",
    "Which financial statement reports a company's revenues and expenses?": "b. Income Statement",
    "What is the term for the process of spreading out investments to reduce risk?": "c. Diversification",
    "What is the abbreviation for the Federal Reserve System in the United States?": "a. Fed",
    "Which financial ratio measures a company's ability to pay its short-term debts?": "b. Current Ratio",
    "True or False: Depreciation is a non-cash expense.": "True"
}

# Questions and answers for Analytics
analytics_questions = {
    "What is data analytics?": "a. The science of analyzing raw data to make conclusions about that information",
    "True or False: Descriptive analytics deals with analyzing data to identify patterns and trends.": "True",
    "What is the primary goal of predictive analytics?": "c. Predict future outcomes based on historical data",
    "Which of the following is a commonly used data visualization tool?": "b. Tableau",
    "What is the process of cleaning and preparing data for analysis called?": "a. Data Wrangling",
    "True or False: Correlation implies causation.": "False",
    "What statistical measure describes the spread of data around the mean?": "b. Standard Deviation",
    "What does KPI stand for?": "c. Key Performance Indicator",
    "Which machine learning technique is used for classification problems?": "d. Decision Trees",
    "What is the process of discovering hidden patterns in large datasets called?": "a. Data Mining"
}

# Questions and answers for Management
management_questions = {
    "What is management?": "c. The process of planning, organizing, leading, and controlling resources to achieve specific goals",
    "True or False: Management is only applicable in business settings.": "False",
    "What does SWOT analysis stand for?": "a. Strengths, Weaknesses, Opportunities, Threats",
    "Which management theory emphasizes the importance of understanding employee needs?": "d. Maslow's Hierarchy of Needs",
    "What is the process of setting goals and determining the best way to achieve them?": "b. Planning",
    "True or False: Leadership and management are interchangeable terms.": "False",
    "What is the term for the formal system of tasks and reporting relationships?": "c. Organizational Structure",
    "What type of power comes from one's position within an organization?": "a. Legitimate Power",
    "What is the term for a situation where two or more people work together to achieve a common goal?": "b. Collaboration",
    "What is the process of monitoring performance and making adjustments as needed?": "d. Controlling"
}

# Questions and answers for Analytic_Thinking
analytic_thinking_questions = {
    "What is critical thinking?": "b. The objective analysis and evaluation of an issue in order to form a judgment",
    "True or False: Analytical thinking is synonymous with creative thinking.": "False",
    "What is the first step in the problem-solving process?": "c. Identify the problem",
    "Which of the following is a common problem-solving technique?": "a. Root Cause Analysis",
    "What is the process of examining assumptions and evidence to form logical conclusions?": "b. Reasoning",
    "True or False: Analytical thinking requires one to accept information at face value.": "False",
    "What is the term for breaking down a complex problem into smaller, manageable parts?": "c. Decomposition",
    "What is the process of generating multiple solutions to a problem?": "d. Brainstorming",
    "True or False: Critical thinking involves only questioning others' ideas.": "False",
    "What is the term for the ability to see situations from multiple perspectives?": "a. Perspective Taking"
}

# Insert data into tables
insert_data("Finance", finance_questions)
insert_data("Analytics", analytics_questions)
insert_data("Management", management_questions)
insert_data("Analytic_Thinking", analytic_thinking_questions)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully!")
