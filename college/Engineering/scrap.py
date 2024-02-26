import csv
import requests
from bs4 import BeautifulSoup

# Read the hrefs from the file
with open('hrefs.txt', 'r') as file:
    hrefs = file.read().splitlines()[3627:]

# Define the CSV file path
csv_file = 'college_data2.csv'

# Write the header row to the CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['College Name', 'Contact no', 'Email', 'Website', 'Address'])  # Add appropriate headers

    for href in hrefs:
        if href:  # Check if href is not empty
            # Make the request and get the page source
            response = requests.get(href)
            page_source = response.text

            # Create BeautifulSoup object
            soup = BeautifulSoup(page_source, 'html.parser')

            # Find div tags with class "block box"
            div_tags = soup.find_all('div', class_='block box')

            # Find li and h2 tags within each div
            for div_tag in div_tags:
                li_tags = div_tag.find_all('li', class_='collegeDetail_detailsIcons__uE8HH')
                h2_tag = div_tag.find('h2')
                if li_tags and h2_tag:
                    li_text = [li_tag.get_text(strip=True) for li_tag in li_tags]
                    h2_text = h2_tag.get_text(strip=True)

                    # Write the data row to the CSV file
                    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow([h2_text] + li_text)
