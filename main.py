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

# Step 5: Example usage
if __name__ == "__main__":
    url_to_scrape = 'https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Fhomepage_milo%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%3A%2F%2Fwww.adobe.com%2Fhome%23old_hash%3D%26from_ims%3Dtrue%3Fclient_id%3Dhomepage_milo%26api%3Dauthorize%26scope%3DAdobeID%2Copenid%2Cgnav%2Cpps.read%2Cfirefly_api%2Cadditional_info.roles%2Cread_organizations%26state%3D%7B%22jslibver%22%3A%22v2-v0.45.0-8-gd14e654%22%2C%22nonce%22%3A%227424714071001927%22%7D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=homepage_milo&scope=AdobeID%2Copenid%2Cgnav%2Cpps.read%2Cfirefly_api%2Cadditional_info.roles%2Cread_organizations&state=%7B"jslibver"%3A"v2-v0.45.0-8-gd14e654"%2C"nonce"%3A"7424714071001927"%7D&relay=00bc0846-25f4-45d6-91a3-c91343dc14e8&locale=en_US&flow_type=token&idp_flow_type=login&s_p=google%2Cfacebook%2Capple%2Cmicrosoft%2Cline&response_type=token&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fwww.adobe.com%2Fhome%23old_hash%3D%26from_ims%3Dtrue%3Fclient_id%3Dhomepage_milo%26api%3Dauthorize%26scope%3DAdobeID%2Copenid%2Cgnav%2Cpps.read%2Cfirefly_api%2Cadditional_info.roles%2Cread_organizations&use_ms_for_expiry=true#/'
    result = find_term_link(url_to_scrape)

    if result:
        print(f"Found link containing 'Terms': {result}")
        print(scrape_content_from_link(result))
    else:
        print("No link containing 'Terms' found")