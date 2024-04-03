import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

# Insert values into Finance table
finance_values = [
    ("What is the basic accounting equation?", "A) Assets = Liabilities + Equity, B) Assets = Equity - Liabilities, C) Assets = Equity + Liabilities", "A) Assets = Liabilities + Equity"),
    ("What is the formula for Return on Investment (ROI)?", "A) (Net Profit / Cost of Investment) x 100%, B) (Net Profit / Revenue) x 100%, C) (Cost of Investment / Net Profit) x 100%", "A) (Net Profit / Cost of Investment) x 100%"),
    ("What is the purpose of a balance sheet?", "A) To show a company's financial position at a specific point in time, B) To forecast future financial performance, C) To evaluate a company's marketing strategies", "A) To show a company's financial position at a specific point in time"),
    ("What is a common measure of liquidity?", "A) Current Ratio, B) Debt-to-Equity Ratio, C) Return on Assets", "A) Current Ratio"),
    ("What does EBITDA stand for?", "A) Earnings Before Interest, Taxes, Depreciation, and Amortization, B) Earnings Before Income, Taxes, Depreciation, and Amortization, C) Earnings Before Interest, Tax, Depreciation, and Assets", "A) Earnings Before Interest, Taxes, Depreciation, and Amortization"),
    ("What does ROI stand for?", "A) Return on Investment, B) Return on Income, C) Revenue on Investment", "A) Return on Investment"),
    ("Which financial statement reports a company's revenues and expenses?", "A) Income Statement, B) Balance Sheet, C) Cash Flow Statement", "A) Income Statement"),
    ("What does GAAP stand for?", "A) Generally Accepted Accounting Principles, B) General Accounting and Auditing Procedures, C) Generally Applied Accounting Policies", "A) Generally Accepted Accounting Principles"),
    ("What is the primary purpose of financial accounting?", "A) To provide information to external users, B) To provide information to internal users, C) To facilitate budgeting and planning", "A) To provide information to external users"),
    ("What is the time value of money concept?", "A) Money received today is worth more than the same amount in the future, B) Money received in the future is worth more than the same amount today, C) Money has no time value", "A) Money received today is worth more than the same amount in the future")
]

cursor.executemany("INSERT INTO Finance (Question, Answer_Choices, Answers) VALUES (?, ?, ?)", finance_values)

# Insert values into Analytics table
analytics_values = [
    ("What is descriptive analytics?", "A) Analyzing historical data to understand past performance, B) Predicting future outcomes based on historical data, C) Identifying trends and patterns in data", "A) Analyzing historical data to understand past performance"),
    ("What is predictive analytics?", "A) Using data and statistical algorithms to predict future outcomes, B) Analyzing historical data to understand past performance, C) Identifying trends and patterns in data", "A) Using data and statistical algorithms to predict future outcomes"),
    ("What is prescriptive analytics?", "A) Recommending actions based on analysis of data, B) Analyzing historical data to understand past performance, C) Identifying trends and patterns in data", "A) Recommending actions based on analysis of data"),
    ("What is the difference between structured and unstructured data?", "A) Structured data is organized and can be easily analyzed, unstructured data lacks organization, B) Structured data lacks organization, unstructured data is easily analyzed, C) Structured and unstructured data are the same", "A) Structured data is organized and can be easily analyzed, unstructured data lacks organization"),
    ("What is data mining?", "A) Extracting useful information from a large dataset, B) Storing data in a database, C) Analyzing data in real-time", "A) Extracting useful information from a large dataset"),
    ("What is the purpose of data visualization?", "A) To present data in a graphical format for easy understanding, B) To encrypt data for secure storage, C) To delete unnecessary data", "A) To present data in a graphical format for easy understanding"),
    ("What is correlation analysis?", "A) Determining the strength of a relationship between two variables, B) Analyzing data to identify outliers, C) Forecasting future trends based on historical data", "A) Determining the strength of a relationship between two variables"),
    ("What is regression analysis?", "A) Predicting a dependent variable based on one or more independent variables, B) Grouping similar data points together, C) Analyzing data to identify trends", "A) Predicting a dependent variable based on one or more independent variables"),
    ("What is clustering analysis?", "A) Grouping similar data points together, B) Analyzing data to identify trends, C) Forecasting future trends based on historical data", "A) Grouping similar data points together"),
    ("What is the role of an analytics dashboard?", "A) To provide a visual overview of key performance indicators, B) To manage databases, C) To conduct data analysis", "A) To provide a visual overview of key performance indicators")
]

cursor.executemany("INSERT INTO Analytics (Question, Answer_Choices, Answers) VALUES (?, ?, ?)", analytics_values)

# Insert values into Management table
management_values = [
    ("What is strategic management?", "A) Process of setting goals and making decisions to achieve them, B) Process of managing day-to-day operations, C) Process of recruiting and hiring employees", "A) Process of setting goals and making decisions to achieve them"),
    ("What is organizational structure?", "A) Framework that defines the hierarchy and reporting relationships within a company, B) Framework for managing projects, C) Framework for marketing products", "A) Framework that defines the hierarchy and reporting relationships within a company"),
    ("What is the purpose of SWOT analysis?", "A) To identify strengths, weaknesses, opportunities, and threats, B) To analyze financial statements, C) To evaluate customer satisfaction", "A) To identify strengths, weaknesses, opportunities, and threats"),
    ("What are the key functions of management?", "A) Planning, organizing, leading, and controlling, B) Marketing, finance, operations, and human resources, C) Sales, production, distribution, and customer service", "A) Planning, organizing, leading, and controlling"),
    ("What is the difference between leadership and management?", "A) Leadership involves inspiring and motivating others, management involves planning and organizing, B) Leadership involves setting goals, management involves implementing plans, C) Leadership involves enforcing rules, management involves decision-making", "A) Leadership involves inspiring and motivating others, management involves planning and organizing"),
    ("What is organizational culture?", "A) Shared values, beliefs, and norms within an organization, B) Organizational structure, C) Marketing strategies", "A) Shared values, beliefs, and norms within an organization"),
    ("What is change management?", "A) Process of managing changes to achieve desired outcomes, B) Process of maintaining the status quo, C) Process of downsizing and restructuring", "A) Process of managing changes to achieve desired outcomes"),
    ("What is the purpose of performance management?", "A) To monitor and improve employee performance, B) To set financial targets, C) To develop marketing strategies", "A) To monitor and improve employee performance"),
    ("What is the role of a manager?", "A) To achieve organizational goals through effective utilization of resources, B) To enforce company policies, C) To handle customer complaints", "A) To achieve organizational goals through effective utilization of resources"),
    ("What is the difference between efficiency and effectiveness?", "A) Efficiency is doing things right, effectiveness is doing the right things, B) Efficiency is doing the right things, effectiveness is doing things right, C) Efficiency and effectiveness are the same", "A) Efficiency is doing things right, effectiveness is doing the right things")
]

cursor.executemany("INSERT INTO Management (Question, Answer_Choices, Answers) VALUES (?, ?, ?)", management_values)

# Insert values into Analytic Thinking table
analytic_thinking_values = [
    ("What is critical thinking?", "A) Process of analyzing and evaluating information to make informed decisions, B) Process of memorizing facts, C) Process of following instructions blindly", "A) Process of analyzing and evaluating information to make informed decisions"),
    ("What is deductive reasoning?", "A) Drawing a specific conclusion from general premises, B) Drawing general conclusions from specific observations, C) Drawing conclusions based on emotions", "A) Drawing a specific conclusion from general premises"),
    ("What is inductive reasoning?", "A) Drawing general conclusions from specific observations, B) Drawing a specific conclusion from general premises, C) Drawing conclusions based on opinions", "A) Drawing general conclusions from specific observations"),
    ("What is logical reasoning?", "A) Using reasoning to reach a valid conclusion, B) Using intuition to make decisions, C) Using emotions to guide decision-making", "A) Using reasoning to reach a valid conclusion"),
    ("What is lateral thinking?", "A) Thinking creatively to solve problems, B) Thinking in a linear and logical manner, C) Thinking based on past experiences", "A) Thinking creatively to solve problems"),
    ("What is analytical thinking?", "A) Breaking down complex problems into smaller components, B) Focusing on the big picture, C) Ignoring details", "A) Breaking down complex problems into smaller components"),
    ("What is systems thinking?", "A) Considering the interconnections and relationships within a system, B) Focusing only on individual components, C) Ignoring the broader context", "A) Considering the interconnections and relationships within a system"),
    ("What is the purpose of critical thinking?", "A) To evaluate arguments and evidence objectively, B) To accept information without questioning it, C) To make decisions based on emotions", "A) To evaluate arguments and evidence objectively"),
    ("What is cognitive bias?", "A) Systematic deviation from rationality in judgment, B) Objective and impartial decision-making, C) Rational decision-making", "A) Systematic deviation from rationality in judgment"),
    ("What is problem-solving?", "A) Process of finding solutions to difficult or complex issues, B) Process of ignoring problems, C) Process of creating problems", "A) Process of finding solutions to difficult or complex issues")
]

cursor.executemany("INSERT INTO Analytic_Thinking (Question, Answer_Choices, Answers) VALUES (?, ?, ?)", analytic_thinking_values)

# Insert values into Apps Development table
apps_development_values = [
    ("What is an IDE?", "A) Integrated Development Environment, B) Internet Development Environment, C) Interactive Design Environment", "A) Integrated Development Environment"),
    ("What is version control?", "A) System for tracking changes to files and managing revisions, B) System for testing software applications, C) System for analyzing code performance", "A) System for tracking changes to files and managing revisions"),
    ("What is an API?", "A) Application Programming Interface, B) Advanced Programming Interface, C) Automated Program Installation", "A) Application Programming Interface"),
    ("What is a database?", "A) Organized collection of data, B) Software for creating graphical user interfaces, C) System for managing network connections", "A) Organized collection of data"),
    ("What is cloud computing?", "A) Delivery of computing services over the internet, B) Storage of data on physical servers, C) Development of software applications", "A) Delivery of computing services over the internet"),
    ("What is agile development?", "A) Iterative approach to software development, B) Linear approach to software development, C) Waterfall approach to software development", "A) Iterative approach to software development"),
    ("What is debugging?", "A) Identifying and fixing errors in code, B) Testing software applications, C) Documenting code", "A) Identifying and fixing errors in code"),
    ("What is user interface design?", "A) Designing interfaces for software applications, B) Designing databases, C) Designing algorithms", "A) Designing interfaces for software applications"),
    ("What is the purpose of unit testing?", "A) Testing individual components of software, B) Testing the entire software application, C) Testing software performance under load", "A) Testing individual components of software"),
    ("What is software deployment?", "A) Process of releasing software for public use, B) Process of designing software, C) Process of analyzing software requirements", "A) Process of releasing software for public use")
]

cursor.executemany("INSERT INTO Apps_Development (Question, Answer_Choices, Answers) VALUES (?, ?, ?)", apps_development_values)

# Commit changes and close connection
conn.commit()
conn.close()

print("Rows inserted successfully.")
