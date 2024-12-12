import requests
from bs4 import BeautifulSoup

# Function to fetch and parse a web page
def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

# Function to scrape data from the page
def scrape_data(soup):
    # Example: Scrape all the headings (h1, h2, h3) from the page
    headings = []
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        headings.append(heading.text.strip())
    return headings

# Main function
def main():
    url = 'https://go2cod.com.et/'  
    soup = fetch_page(url)
    if soup:
        data = scrape_data(soup)
        print("Scraped Data:")
        for item in data:
            print(item)

if __name__ == '__main__':
    main()
