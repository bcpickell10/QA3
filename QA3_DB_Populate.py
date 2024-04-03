import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

# Sample data for each table
finance_data = [
    ('True/False: The return on investment (ROI) is calculated by dividing the net profit by the initial investment.', 'True, False', 'True'),
    ('Multiple Choice: Which of the following is NOT a type of financial statement? Income Statement, Balance Sheet, Cash Flow Statement, Profit & Loss Statement', 'Profit & Loss Statement, Cash Flow Statement, Income Statement, Balance Sheet', 'Profit & Loss Statement'),
    ('True/False: The stock market crash of 1929 led to the Great Depression in the United States.', 'True, False', 'True'),
    ('True/False: A budget deficit occurs when government spending exceeds revenue.', 'True, False', 'True'),
    ('Multiple Choice: Which of the following is a measure of a company\'s liquidity? Quick Ratio, Asset Turnover Ratio, Debt-to-Equity Ratio, Return on Assets', 'Asset Turnover Ratio, Return on Assets, Debt-to-Equity Ratio, Quick Ratio', 'Quick Ratio'),
    ('True/False: Inflation refers to a sustained increase in the general price level of goods and services over time.', 'True, False', 'True'),
    ('Multiple Choice: What is the primary function of an investment bank? Underwriting Securities, Consumer Banking, Asset Management, Retail Banking', 'Consumer Banking, Retail Banking, Asset Management, Underwriting Securities', 'Underwriting Securities'),
    ('True/False: A mutual fund pools money from many investors to invest in a diversified portfolio of stocks, bonds, or other securities.', 'True, False', 'True'),
    ('Multiple Choice: What is the main goal of financial management? Maximize Profit, Maximize Revenue, Minimize Costs, Maximize Market Share', 'Maximize Revenue, Minimize Costs, Maximize Market Share, Maximize Profit', 'Maximize Profit'),
    ('True/False: The time value of money principle states that a dollar today is worth more than a dollar in the future.', 'True, False', 'True')
]

analytics_data = [
    ('True/False: Descriptive analytics focuses on what has happened in the past.', 'True, False', 'True'),
    ('Multiple Choice: Which of the following is a statistical measure of the dispersion or spread of data?', 'Mean, Median, Range, Standard Deviation', 'Range'),
    ('True/False: Predictive analytics uses historical data to predict future outcomes.', 'True, False', 'True'),
    ('Multiple Choice: What is the purpose of clustering analysis in data analytics? Grouping Similar Data, Identifying Outliers, Calculating Averages, Estimating Trends', 'Identifying Outliers, Calculating Averages, Estimating Trends, Grouping Similar Data', 'Grouping Similar Data'),
    ('True/False: Data visualization is a process of presenting data in graphical or pictorial formats.', 'True, False', 'True'),
    ('Multiple Choice: Which of the following is NOT a type of data visualization? Scatter Plot, Histogram, Decision Tree, Heat Map', 'Decision Tree, Scatter Plot, Heat Map, Histogram', 'Decision Tree'),
    ('True/False: Correlation measures the strength and direction of the relationship between two variables.', 'True, False', 'True'),
    ('Multiple Choice: Which statistical method is used to determine the strength of association between two variables? Pearson Correlation Coefficient, Chi-Square Test, T-Test, ANOVA', 'Chi-Square Test, T-Test, ANOVA, Pearson Correlation Coefficient', 'Pearson Correlation Coefficient'),
    ('True/False: Data mining is the process of extracting patterns from large datasets.', 'True, False', 'True'),
    ('Multiple Choice: What is the primary goal of data preprocessing? Data Reduction, Data Integration, Data Transformation, Data Cleaning', 'Data Integration, Data Transformation, Data Cleaning, Data Reduction', 'Data Cleaning')
]

management_data = [
    ('True/False: Autocratic leadership style involves high levels of participation from team members in decision-making processes.', 'True, False', 'False'),
    ('Multiple Choice: Which of the following is NOT a function of management? Planning, Organizing, Leading, Observing', 'Observing, Leading, Planning, Organizing', 'Observing'),
    ('True/False: The SWOT analysis framework is used to assess a company\'s internal strengths and weaknesses, as well as external opportunities and threats.', 'True, False', 'True'),
    ('Multiple Choice: What is the primary focus of strategic management? Long-Term Planning, Short-Term Execution, Operational Efficiency, Tactical Decision Making', 'Short-Term Execution, Operational Efficiency, Tactical Decision Making, Long-Term Planning', 'Long-Term Planning'),
    ('True/False: Organizational culture refers to the values, beliefs, and norms shared by members of an organization.', 'True, False', 'True'),
    ('Multiple Choice: Which of the following is NOT a characteristic of effective organizational culture? Hierarchical Structure, Innovation, Employee Engagement, Clear Communication', 'Hierarchical Structure, Innovation, Employee Engagement, Clear Communication', 'Hierarchical Structure'),
    ('True/False: Total Quality Management (TQM) focuses on continuous improvement of product and service quality.', 'True, False', 'True'),
    ('Multiple Choice: What is the purpose of performance appraisal in management? Evaluate Employee Performance, Increase Employee Morale, Set Salary Levels, Promote Team Collaboration', 'Increase Employee Morale, Set Salary Levels, Promote Team Collaboration, Evaluate Employee Performance', 'Evaluate Employee Performance'),
    ('True/False: Outsourcing involves delegating certain business functions or processes to external vendors or third-party providers.', 'True, False', 'True'),
    ('Multiple Choice: What is the primary goal of supply chain management? Reduce Costs, Maximize Sales, Improve Product Quality, Increase Market Share', 'Maximize Sales, Improve Product Quality, Increase Market Share, Reduce Costs', 'Reduce Costs')
]

analytic_thinking_data = [
    ('True/False: Critical thinking is a form of linear, step-by-step reasoning.', 'True, False', 'False'),
    ('Multiple Choice: Which of the following is NOT a characteristic of effective critical thinkers? Open-mindedness, Creativity, Rigidity, Systematicity', 'Rigidity, Creativity, Open-mindedness, Systematicity', 'Rigidity'),
    ('True/False: Analytical thinking involves breaking down complex problems into smaller components.', 'True, False', 'True'),
    ('Multiple Choice: What is the primary goal of analytical thinking? Problem Solving, Decision Making, Strategic Planning, Creative Thinking', 'Decision Making, Strategic Planning, Creative Thinking, Problem Solving', 'Problem Solving'),
    ('True/False: Systems thinking emphasizes understanding the interactions and interdependencies within complex systems.', 'True, False', 'True'),
    ('Multiple Choice: Which of the following is NOT a step in the systems thinking process? Identify Feedback Loops, Analyze Cause-and-Effect Relationships, Implement Solutions, Evaluate Feedback Effects', 'Implement Solutions, Analyze Cause-and-Effect Relationships, Evaluate Feedback Effects, Identify Feedback Loops', 'Implement Solutions'),
    ('True/False: Metacognition involves reflecting on one\'s own thought processes and cognitive strategies.', 'True, False', 'True'),
    ('Multiple Choice: Which of the following is NOT a component of metacognition? Knowledge of Strategies, Awareness of Problem-Solving Techniques, Self-Regulation, Knowledge of Facts', 'Awareness of Problem-Solving Techniques, Knowledge of Facts, Self-Regulation, Knowledge of Strategies', 'Awareness of Problem-Solving Techniques'),
    ('True/False: Divergent thinking focuses on finding a single correct solution to a problem.', 'True, False', 'False'),
    ('Multiple Choice: What is the primary purpose of divergent thinking? Generate Creative Ideas, Analyze Data, Make Logical Deductions, Solve Mathematical Problems', 'Analyze Data, Make Logical Deductions, Solve Mathematical Problems, Generate Creative Ideas', 'Generate Creative Ideas')
]

apps_development_data = [
    ('True/False: Object-oriented programming (OOP) emphasizes code reusability and modular programming.', 'True, False', 'True'),
    ('Multiple Choice: Which programming language is commonly used for Android app development? Java, C++, Python, Swift', 'Python, Java, C++, Swift', 'Java'),
    ('True/False: Cross-platform app development allows developers to build apps that run on multiple operating systems.', 'True, False', 'True'),
    ('Multiple Choice: Which of the following is a popular cross-platform mobile app development framework? React Native, Xamarin, Flutter, Ionic', 'Flutter, Xamarin, Ionic, React Native', 'React Native'),
    ('True/False: Agile software development emphasizes adaptive planning, evolutionary development, and early delivery.', 'True, False', 'True'),
    ('Multiple Choice: Which agile methodology uses short iterations called sprints? Scrum, Kanban, Lean, Extreme Programming (XP)', 'Kanban, Lean, Extreme Programming (XP), Scrum', 'Scrum'),
    ('True/False: Test-driven development (TDD) involves writing tests before writing the actual code.', 'True, False', 'True'),
    ('Multiple Choice: Which software testing technique involves testing individual units or components of a software application? Unit Testing, Integration Testing, System Testing, Acceptance Testing', 'Integration Testing, System Testing, Acceptance Testing, Unit Testing', 'Unit Testing'),
    ('True/False: Continuous integration (CI) involves automatically building and testing code changes as they are committed to a shared repository.', 'True, False', 'True'),
    ('Multiple Choice: Which version control system is commonly used for collaborative software development? Git, Subversion (SVN), Mercurial, CVS', 'Subversion (SVN), Mercurial, CVS, Git', 'Git')
]

# Insert sample data into each table
cursor.executemany('INSERT INTO Finance VALUES (?, ?, ?)', finance_data)
cursor.executemany('INSERT INTO Analytics VALUES (?, ?, ?)', analytics_data)
cursor.executemany('INSERT INTO Management VALUES (?, ?, ?)', management_data)
cursor.executemany('INSERT INTO Analytic_Thinking VALUES (?, ?, ?)', analytic_thinking_data)
cursor.executemany('INSERT INTO Apps_Development VALUES (?, ?, ?)', apps_development_data)

# Commit the changes and close the connection
conn.commit()
conn.close()
