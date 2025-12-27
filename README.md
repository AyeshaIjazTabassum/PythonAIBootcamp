# Python and AI Bootcamp
**Course Outline**
**Duration:** _6 Weeks_ | **Schedule:** _5 sessions/week (Monday-Friday)_

# Week 1: Python Fundamentals & Data Handling
**Day 1: Python Basics I**

- Variables, Numbers, Strings
- Basic operations and string methods
- Interactive coding exercises with variables and strings

**Day 2: Python Basics II**
  
- Lists, Dictionaries, Tuples
- Basic operations and methods
- Data structure manipulation exercises

**Day 3: Control Structures**
- If conditions and logical operators
- For loops and while loops
- Loop exercises and conditional logic
- Build a number guessing game

**Day 4: Functions & Error Handling**
- Functions, parameters, return values
- Local and Global variables
- File handling as read, write, append

**Day 5: Web Scraping**
- Web Scraping, HTTP requests and HTML structure
- BeautifulSoup basics
- Scrape a simple website
- Extract and save data to CSV/JSON
# Assignment Week-1
**TASK 1: PYTHON BASICS & VARIABLES**
- Take user input for:
  - Name
  - Age
  - Favorite Programming Language
- Display the output using formatted strings (f-strings).
- Print the data type of each variable.

**TASK 2: CONTROL FLOW & LOGIC BUILDING**
- Ask the user to enter a number.
- Determine and display:
  - Whether the number is positive, negative, or zero.
  - Whether the number is even or odd.
- Handle invalid input using try-except blocks.

**TASK 3: LOOPS & PATTERN GENERATION**
- Print all prime numbers between 1 and 100.
- Use nested loops where applicable.

**TASK 4: FUNCTIONS & MODULAR PROGRAMMING**
- Build a function-based calculator that supports:
  - Addition
  - Subtraction
  - Multiplication
  - Division (handle division by zero)
- Implement a menu-driven interface.
- Each operation must be implemented as a separate function.

**TASK 5: INTRO TO AI THINKING WITH PYTHON**
- Create a dataset of students containing:
  - Student Name
  - Marks
- Calculate and display:
  - Average marks
  - Highest score
  - Lowest score
- Classify student performance using the following rules:
  - Marks 80 or above → Excellent
  - Marks between 60 and 79 → Good
  - Below 60 → Needs Improvement
 
**TASK 6: WEB SCRAPING WITH PYTHON**
- Use the requests and BeautifulSoup libraries.
- Scrape data from a public website (such as quotes, headlines, job titles, or product names).
- Extract at least:
  - Title or heading
  - Description or related text
  - Store the scraped data in a Python list or dictionary.
- Display the extracted data in a clean and readable format.
- Bonus (Optional): Save the scraped data into a .txt or .csv file.

# Week 2: Data Analysis & Machine Learning Foundations
**Day 6: Data Analysis with Pandas**
- Introduction to NumPy and Pandas
- DataFrames and basic operations
- Load and explore the scraped data from weekend
- Basic data cleaning operations

**Day 7: Exploratory Data Analysis**
- Data visualization with Matplotlib/Seaborn
- Handling missing values and outliers
- Create meaningful visualizations

**Day 8: Introduction to Machine Learning**
- Supervised vs Unsupervised learning
- Training, validation, testing concepts
- Prepare data for machine learning
- Train-test split and basic preprocessing

**Day 9: Classification - KNN**
- K-Nearest Neighbors algorithm
- Model evaluation metrics
- Implement KNN classifier
- Evaluate with confusion matrix and accuracy

**Day 10: Classification - Decision Trees**
- Decision Trees and Random Forest
- Feature importance
- Build and compare multiple classification models

# Assignment Week-2
**Task 1: Data Loading & Cleaning (Pandas)**
- Students must:
  - Load the dataset using Pandas
  - Check missing values and duplicates
  - Handle missing or incorrect data
- Reasoning Questions:
  - Why is data cleaning a critical step before EDA and model training?
  - What problems can incorrect or missing medical data cause in predictions?
  - Which cleaning decision had the biggest impact on your dataset?

**Task 2: Exploratory Data Analysis (EDA)**
- Students must visualize:
  - Age distribution (Histogram)
  - Gender vs Heart Disease (Bar chart)
  - Cholesterol outliers (Boxplot)
  - Feature correlation (Heatmap)
- Reasoning Quesions:
  - Which age group appears to have the highest heart disease risk? Why?
  - Does cholesterol alone seem sufficient to predict heart disease?
  - Which features appear most strongly related to the target?
  - How can outliers affect model performance in medical datasets?

**Task 3: Machine Learning Preprocessing**
- Students must:
  - Separate features (X) and target (y)
  - Apply train–test split
  - Apply feature scaling
- Reasoning Questions:
  - Why do we split data into training and testing sets?
  - Why is feature scaling necessary before applying KNN?
  - What is data leakage, and how does preprocessing help prevent it?

**Task 4: KNN Classification**
- Students must:
  - Train KNN classifier
  - Experiment with multiple values of K
  - Evaluate using accuracy and confusion matrix
- Reasoning Questions:
  - How does the value of K influence bias and variance?
  - Why does KNN performance change after scaling?
  - What are the limitations of KNN in a healthcare setting?

**Task 5: Decision Tree & Random Forest**
- Students must:
  - Train a Decision Tree classifier
  - Train a Random Forest classifier
  - Extract feature importance
- Reasoning Questions:
  - Which model performed better: Decision Tree or Random Forest? Why?
  - Which health-related feature was most important and why?
  - Why is Random Forest considered more stable and reliable than a single tree?

**Task 6: Model Comparison & Recommendation**
- Students must:
  - Compare KNN, Decision Tree, and Random Forest
  - Plot accuracy comparison
  - Recommend a final model
- Reasoning Questions:
  - Which model worked best overall, and what explains its performance?
  - Which model would you recommend for real hospital deployment and why?
  - What did you learn about ML model behavior from this case study?
  - How could this system be improved in future work?
 
# Week 3: Advanced Machine Learning & Deep Learning Intro
**Day 11: Regression Models**
- Linear Regression concepts
- Regression evaluation metrics (MSE, RMSE, R²)
- Build linear regression model
