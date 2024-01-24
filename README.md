# Sentiment Analysis and Text Similarity
This project is designed for sentiment analysis on Amazon product reviews. It utilizes SpaCy and TextBlob libraries to analyze sentiments and calculate the similarity score between reviews.

# Importance
Understanding customer sentiments in product reviews is crucial for businesses to enhance product quality and customer satisfaction. The project streamlines this process by providing a tool for sentiment analysis and textual similarity comparison.

# Table of Contents
1. Prerequisites
2. Usage
3. Code Explanation
4. Contributing
5. License

# Prerequisites
Ensure the following libraries are installed:
- spaCy
- pandas
- textblob

# Install dependencies with:
bash
Copy code
pip install spacy pandas textblob

# Download the spaCy English model:
bash
Copy code
python -m spacy download en_core_web_sm
Usage

# Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/your-repo.git
cd your-repo
Install necessary libraries as per the Prerequisites.


# Run the Script:

# Execute the script:

- bash
Copy code
python sentiment_analysis.py
This will perform sentiment analysis on reviews and print results along with the similarity score between two selected reviews.

# Code Explanation
- Import spaCy, pandas, and TextBlob.
- Load spaCy's English model (en_core_web_sm).
- Load Amazon product reviews from the CSV file.
- Clean the data by removing missing values.
- Define analyze_sentiment function for sentiment analysis using spaCy for data preprocessing and TextBlob for scoring.
- Test sentiment analysis on sample reviews.
- Choose two reviews for comparison and calculate the similarity score with spaCy's similarity function.

# Contributing
Contributions, issues, and feature requests are welcome. Feel free to submit a pull request.

# License
This project is licensed under the MIT License.






