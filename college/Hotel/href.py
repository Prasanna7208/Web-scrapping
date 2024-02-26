import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser

# Load the webpage
url = 'https://www.collegedekho.com/hospitality-aviation/colleges-in-india/'
driver.get(url)

# Wait for the page to load and the "Load More" button to appear
wait = WebDriverWait(driver, 10)
load_more_button = wait.until(EC.visibility_of_element_located((By.ID, 'loadMoreButton')))

# Extract href links and save them after each "Load More" button click
downloaded_colleges = set()  # Track the already downloaded colleges
while True:
    driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
    time.sleep(2)  # Wait for scrolling to complete
    driver.execute_script("arguments[0].click();", load_more_button)
    time.sleep(2)  # Wait for the newly loaded colleges to appear

    # Get the page source
    page_source = driver.page_source

    # Create BeautifulSoup object
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all div elements with class "title"
    div_titles = soup.find_all('div', class_='title')

    # Extract href from the 'a' tag within each div
    href_list = []
    for div_title in div_titles:
        a_tag = div_title.find('a')
        if a_tag and 'href' in a_tag.attrs:
            href = 'https://www.collegedekho.com' + a_tag['href']
            if href not in downloaded_colleges:
                href_list.append(href)
                downloaded_colleges.add(href)

    # Save the extracted hrefs to a file after each iteration
    with open('hrefs.txt', 'a') as file:  # Append mode to add new links without overwriting
        file.write('\n'.join(href_list) + '\n')

    # Check if the "Load More" button is still visible
    load_more_button = driver.find_element(By.ID, 'loadMoreButton')
    if not load_more_button.is_displayed():
        break

# Close the browser
driver.quit()
