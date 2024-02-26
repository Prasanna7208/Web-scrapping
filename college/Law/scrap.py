import csv
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Initialize Selenium webdriver
driver = webdriver.Chrome()  # Replace with the appropriate webdriver for your browser

# Read the hrefs from the file
with open('hrefs.txt', 'r') as file:
    hrefs = file.read().splitlines()

# Define the CSV file path
csv_file = 'Law_college_data.csv'

# Write the header row to the CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['College Name', 'Contact no', 'Email', 'Website', 'Address'])  # Add appropriate headers

    for href in hrefs:
        if href:  # Check if href is not empty
            # Use Selenium to make the request
            driver.get(href)
            time.sleep(3)  # Add a delay to allow the page to load

            # Get the page source from Selenium
            page_source = driver.page_source

            # Create BeautifulSoup object
            soup = BeautifulSoup(page_source, 'html.parser')

            # Find div tags with class "block box"
            div_tags = soup.find_all('div', class_='block box')

            # Initialize a list to store the data for the current link
            college_data = []

            for div_tag in div_tags:
                li_tags = div_tag.find_all('li', class_='collegeDetail_detailsIcons__uE8HH')
                h2_tag = div_tag.find('h2')
                if li_tags and h2_tag:
                    li_text = [li_tag.get_text(strip=True) for li_tag in li_tags]
                    h2_text = h2_tag.get_text(strip=True)

                    college_data.extend([h2_text] + li_text)

            # Write the data row to the CSV file
            with open(csv_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(college_data)

# Quit the Selenium webdriver
driver.quit()
