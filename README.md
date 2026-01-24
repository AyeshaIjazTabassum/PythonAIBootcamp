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

**Day 12: Advanced Classification**
- Logistic Regression
- Ensemble methods overview
- Implement logistic regression
- Evaluation Matrices

**Day 13: Unsupervised Learning**
- Clustering concepts
- K-means and hierarchical clustering
- Flower segmentation project
- Cluster evaluation and visualization

**Day 14: Neural Networks Basics**
- Neural network fundamentals
- Activation functions and backpropagation
- Build simple neural network with scikit-learn
- Compare with traditional ML models

**Day 15: Deep Learning with TensorFlow**
- Introduction to TensorFlow/Keras
- Deep neural networks
- Build first deep learning model
- Train on images data

# Assignment Week-3
**Task**
- Build a deep learning model using TensorFlow/Keras and for a real-world dataset.
- Dataset choice is yours; you can utilize sources like Kaggle or datasets of keras.

# Week 4: Computer Vision & NLP
**Day 16: Image Processing Basics**
- Image data handling
- Basic image preprocessing
- Load and manipulate images
- Basic image transformations

**Day 17: Convolutional Neural Networks**
- CNN architecture and concepts
- Convolution, pooling, and filters

**Day 18: Convolutional Neural Networks Practice**
- CNN concepts
- Build CNN for image classification
- MNIST dataset

**Day 19: Transfer Learning**
- Transfer learning concepts
- Pre-trained models (ResNet, EfficientNet)
- Fine-tune pre-trained model
- Custom image classification project

**Day 20: NLP Fundamentals**
- Text preprocessing (tokenization, stemming)
- TF-IDF and word embeddings
- Clean and preprocess text data
- Naive Bayes for text
- Sentiment analysis concepts
# Assignment Week-4
**1. CNN (Convolutional Neural Networks)**
  - Project: Cat vs Dog Image Classifier
  - Dataset: Kaggle Cats vs Dogs
  - Goal: Binary image classification

**2. Transfer Learning**
  - Project: Flower Species Classification 
  - Dataset: TensorFlow Flowers Dataset
  - Model: MobileNetV2 / ResNet50 (pretrained)

**3. NLP Project**
  - Project: Spam Email / SMS Detection
  - Dataset: SMS Spam Collection
  - Goal: Spam vs Ham
  - Bag of Words / TF-IDF
  - Naive Bayes / Logistic Regression

# Week 5: Generative AI & Prompt Engineering
**Day 21: Introduction to Generative AI**
- What is Generative AI?
- Differences from discriminative models
- Explore different generative AI tools

**Day 22: Prompt Engineering**
- Effective prompting techniques
- Zero-shot, few-shot, chain-of-thought
- Practice prompt engineering
- Build prompt templates

**Day 23: Working with AI APIs**
- Google Generative AI SDK
- System prompts and persona development
- Build applications using AI APIs
- Create different AI personas

**Day 24: Multimodal AI**
- Speech to image model
- Build voice-to-art application
- Experiment with multimodal workflows

**Day 25: Advanced Generative Techniques**
- CLIP and BLIP models
- Multimodal understanding
- Build image search system
- Visual question answering

# Assignment Week-5
Build a Chatbot on Hugging Face that includes atleast one of the following features:
- Multimodality
- Use of CLIP or BLIP 
- Different Personas

# Week 6: Agentic AI & Multi-Agent Systems
**Day 26: Introduction to AI Agents**
- What are AI agents?
- Agents vs chatbots
- Agent capabilities (tools, memory, reasoning)
- Set up LangChain environment
- Build first simple agent

**Day 27: LangChain Fundamentals**
- Chains, tools, and memory in LangChain
- Agent architectures
- Create agents with different tools
- Memory and conversation history

**Day 28: Advanced Agent Capabilities**
- Tool usage and function calling
- Reasoning and decision-making
- Build research assistant agent

**Day 29: Multi-Agent Systems**
- Introduction to CrewAI
- Multi-agent coordination
- Set up first multi-agent system
- Define agent roles and responsibilities
