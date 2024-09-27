import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://brdhar.com/publications/"


response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

soup = BeautifulSoup(response.text, 'html.parser')

publication_data = []
articles = soup.find_all('li')  

for article in articles:
    # Extract title
    title = article.text.strip()

    # Extract publication year 
    date_tag = article.find('time')
    if date_tag:
        year = date_tag.text.strip().split()[-1]  # Extract the year
    else:
        year = "Unknown"

    # Extract publisher name 
    publisher_tag = article.find('span', class_='publisher')  
    publisher = publisher_tag.text.strip() if publisher_tag else "Unknown"

    # Extract topics 
    topics_tag = article.find('div', class_='topics')  
    if topics_tag:
        topics = ", ".join([topic.text for topic in topics_tag.find_all('span')])  
        topics = "Unknown"

    # Append extracted data to the list
    publication_data.append([title, year, publisher, topics])

# Create a DataFrame to store publication data
df = pd.DataFrame(publication_data, columns=['Title', 'Year', 'Publisher', 'Topics'])

# Save the DataFrame to a CSV file
df.to_csv('publication_archive_data.csv', index=False)

print("Data extraction complete. The publication data has been saved to 'publication_archive_data.csv'.")
