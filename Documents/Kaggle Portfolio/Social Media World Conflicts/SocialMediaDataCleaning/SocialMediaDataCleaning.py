import pandas as pd
import re

# Load the dataset
file_path = r'C:\Users\EssexOsama\Documents\Kaggle Portfolio\Social Media World Conflicts\conflicts_hashtag_search_raw.csv'
data = pd.read_csv(file_path)

# Inspect the Data
print(f"Shape of the dataset: {data.shape}")
print("Missing values in each column:")
print(data.isnull().sum())
duplicates = data.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
print("Data types of each column:")
print(data.dtypes)

# Handle Missing Values
# Fill missing values for text fields with 'No content'
data['text'].fillna('No content', inplace=True)

# Fill missing values with 0 for numerical columns
data['likesCount'].fillna(0, inplace=True)
data['commentsCount'].fillna(0, inplace=True)
data['viewsCount'].fillna(0, inplace=True)

# Normalize Text Data
def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    text = text.strip()  # Remove leading and trailing spaces
    return text

data['text'] = data['text'].apply(clean_text)
data['text'] = data['text'].str.lower()

# Convert Data Types
data['creationDate'] = pd.to_datetime(data['creationDate'], errors='coerce')

# Check if conversion was successful
print("Data types after conversion:")
print(data.dtypes)

# Optional: Save cleaned data to a new CSV file
cleaned_file_path = r'C:\Users\EssexOsama\Documents\Kaggle Portfolio\Social Media World Conflicts\cleaned_data.csv'
data.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to {cleaned_file_path}.")
