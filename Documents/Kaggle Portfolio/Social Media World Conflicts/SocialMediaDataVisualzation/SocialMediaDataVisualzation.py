import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
cleaned_file_path = r'C:\Users\EssexOsama\Documents\Kaggle Portfolio\Social Media World Conflicts\cleaned_data.csv'
data = pd.read_csv(cleaned_file_path)

# Check if the 'conflict' column exists instead of 'input'
if 'input' in data.columns:
    data.rename(columns={'input': 'conflict'}, inplace=True)

# Set Seaborn style for better aesthetics
sns.set(style='whitegrid')

# Example 1: Bar plot of average likes by conflict
plt.figure(figsize=(10, 6))
avg_likes = data.groupby('conflict')['likesCount'].mean().reset_index()
sns.barplot(data=avg_likes, x='conflict', y='likesCount', palette='husl')

# Add annotations for average likes
for index, row in avg_likes.iterrows():
    plt.text(index, row['likesCount'], round(row['likesCount'], 2), ha='center', va='bottom')

plt.title('Average Likes by Conflict')
plt.xlabel('Conflict')
plt.ylabel('Average Likes')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
plt.savefig(r'C:\Users\EssexOsama\Documents\Kaggle Portfolio\Social Media World Conflicts\average_likes_by_conflict.png')
plt.show()

# Example 2: Histogram of likes count
plt.figure(figsize=(10, 6))
sns.histplot(data['likesCount'], bins=30, kde=True, color='blue')
plt.title('Distribution of Likes Count')
plt.xlabel('Likes Count')
plt.ylabel('Frequency')
plt.tight_layout()

# Save the histogram
plt.savefig(r'C:\Users\EssexOsama\Documents\Kaggle Portfolio\Social Media World Conflicts\likes_distribution.png')
plt.show()

# Example 3: Box plot for likes count by conflict
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='conflict', y='likesCount', palette='husl')
plt.title('Box Plot of Likes Count by Conflict')
plt.xlabel('Conflict')
plt.ylabel('Likes Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the box plot
plt.savefig(r'C:\Users\EssexOsama\Documents\Kaggle Portfolio\Social Media World Conflicts\likes_box_plot.png')
plt.show()
