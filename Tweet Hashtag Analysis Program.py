# Tweet Hashtag Analysis Program

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: list of tweets
tweets = [
    "Learning Python is fun! #coding #python",
    "INST126 gives you a good introduction to Python! #coding #python #datascience",
    "Data science with #python is cool #datascience #coding",
    "Matplotlib makes plotting easy! #python #matplotlib",
    "#numpy is powerful for numerical computations #python",
    "Regular expressions in #python #coding"
]

# Extract hashtags using regular expressions
# I used the re.findall() function to search for patterns that match hashtags
hashtags = []
for tweet in tweets:
    hashtags.extend(re.findall(r"#(\w+)", tweet))

# Creating a DataFrame using Pandas
# I created a DataFrame to store and manipulate the extracted hashtags
# Each hashtag becomes a row in the DataFrame
df = pd.DataFrame(hashtags, columns=['Hashtag'])

# Data Aggregation: Count the frequency of each hashtag
# Pandas value_counts() function provides a simple way to get the count of each hashtag
hashtag_counts = df['Hashtag'].value_counts()

# NumPy: Perform numerical operations (if needed)
# This part can be used for additional numerical analysis like normalization

# Matplotlib: Visualize the data
# We create a bar plot to display the frequency of the top 10 hashtags
top_hashtags = hashtag_counts.head(10)
plt.figure(figsize=(10, 6))
top_hashtags.plot(kind='bar')
plt.title('Top 10 Hashtags in Tweets')
plt.xlabel('Hashtag')
plt.ylabel('Frequency')
plt.show()