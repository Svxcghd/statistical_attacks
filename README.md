# statistical_attacks
This project implements a basic frequency analysis using n-grams in Python. The objective is to divide a given text into sequences of length n (n-grams) and calculate the frequency of each occurrence, displaying the results in a structured table using pandas.
This technique is commonly used in classical cryptography, statistical text analysis, and natural language processing (NLP).
How It Works

The program performs the following steps:

First, it removes spaces from the input text to work with a continuous string.
Then, it generates n-grams using a sliding window of size n.
After that, it uses collections.Counter to compute the frequency of each n-gram.
Finally, it creates a pandas DataFrame to display the results ordered by frequency.

Technologies Used

Python 3
collections (Counter)
pandas

Installation
To run this project, make sure pandas is installed use this command in terminal to verificate that pandas is already installed
pip install pandas
