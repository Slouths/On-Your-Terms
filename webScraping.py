from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Step 1: Set up Selenium WebDriver
def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run browser in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Step 3: Scrape content from the extracted links
def scrape_content_from_link(link):
    try:
        response = requests.get(link, timeout=10)
        response.raise_for_status()  # Check for HTTP request errors
        soup = BeautifulSoup(response.text, "html.parser")

        # Example: Extract all text content from the page
        page_text = soup.get_text(separator="\n")
        return page_text.strip()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {link}: {e}")
        return None


def find_term_link(url, search_term="Terms"):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

    # Set up the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the page
        driver.get(url)

        # Wait for the page to load and find the first link containing the search term
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), '{search_term}')]"))
        )

        # Get the href attribute of the found element
        href = element.get_attribute("href")
        
        return href

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        driver.quit()

