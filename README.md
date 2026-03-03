Statistical Attacks – N-Gram Frequency Analysis (Python)

📌 Description: 
This project implements a basic frequency analysis using n-grams in Python.  
The objective is to divide a given text into sequences of length n (n-grams), calculate the frequency of each occurrence, and display the results in a structured table using pandas.  
This technique is commonly used in:  
Classical cryptography  
Statistical text analysis  
Natural Language Processing (NLP)  
Cryptanalysis of substitution ciphers  

🎯 Objective: 
The purpose of this project is to:  
Understand how n-gram frequency analysis works  
Apply statistical techniques to text data  
Simulate classical cryptanalysis approaches  
Practice data visualization using pandas  

🛠 Concepts Used:  
String manipulation  
Sliding window technique  
collections.Counter for frequency counting  
Data analysis with pandas  
Basic cryptographic analysis concepts  

⚙️ How It Works: 
The program performs the following steps: 
Removes spaces from the input text to create a continuous string.  
Generates n-grams using a sliding window of size n.  
Uses collections.Counter to compute the frequency of each n-gram.  
Creates a pandas DataFrame to display the results ordered by frequency.  

▶️ Installation: 
Make sure you have Python 3 installed.  
This project requires pandas.  
To verify or install pandas, run:  
pip install pandas  

▶️ Usage: 
Run the script with: 
python statistical_attacks.py  
You can modify the input text or n-gram size directly inside the script depending on your analysis needs.  

📊 Example Output (Conceptual)  
N-Gram	Frequency  
TH	15  
HE	12  
ER	10  

📚 What I Learned: 
How frequency analysis supports classical cryptanalysis  
How to implement sliding window logic in Python  
How statistical patterns reveal language structure  
How to organize and display results using pandas  

🚀 Possible Improvements: 
Add graphical visualization (bar charts with matplotlib)  
Support reading directly from external files  
Normalize frequencies (relative frequency %)  
Support different preprocessing options (lowercase, punctuation removal)  
Compare frequency distribution against known English letter frequencies  

📝 Notes: 
For the frequency analyzer with file and ciphertext, it is necessary to put the text or the file in the same directory where the frequency analyzer script is located.  
