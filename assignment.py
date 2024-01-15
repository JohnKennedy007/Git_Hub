import os
import requests
from bs4 import BeautifulSoup

def scrape_medium_article(url):
    # Send a GET request to the provided URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and extract the main text content
        article_text = ""
        for paragraph in soup.find_all('p'):
            article_text += paragraph.get_text() + "\n"

        # Create a text file and write the extracted text into it
        file_name = "medium_article.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(article_text)

        print(f"Web scraping successful. Text saved to {file_name}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    # Example usage:
    # Replace 'your_medium_article_url' with the actual Medium article URL you want to scrape
    article_url = input("Enter the Medium article URL: ")
    scrape_medium_article(article_url)
