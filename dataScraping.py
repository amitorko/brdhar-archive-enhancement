# dataScraping.py
import requests
from bs4 import BeautifulSoup
import csv

def scrape_data():
    # URL of the page to scrape
    url = 'https://brdhar.com/'
    # request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    tags_to_extract = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    for tag_name in tags_to_extract:
        for element in soup.find_all(tag_name):
            data.append([tag_name, element.text.strip()])

    # Write data to a CSV file
    csv_file_path = 'extracted_data.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Tag', 'Text'])  # Column headers
        writer.writerows(data)

    print('Webpage data has been written to CSV.')

def parse_log_file(log_file_path):
    
    logs = []
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()  
            if len(parts) > 9:  # Simple check to avoid malformed lines
                log_entry = {
                    'ip': parts[0],
                    'datetime': parts[3] + parts[4],
                    'request': parts[5] + ' ' + parts[6] + ' ' + parts[7],
                    'status': parts[8],
                    'size': parts[9],
                }
                logs.append(log_entry)
    return logs


if __name__ == "__main__":
    scrape_data()
    
