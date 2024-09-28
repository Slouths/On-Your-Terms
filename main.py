from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


# Step 2: Get links from a dynamic webpage
def get_links_from_dynamic_page(url):
    driver = initialize_driver()
    driver.get(url)

    # Example: get all links (<a> tags) from the dynamic webpage
    links = driver.find_elements(By.TAG_NAME, "a")
    hrefs = [link.get_attribute("href") for link in links if link.get_attribute("href")]

    driver.quit()
    return hrefs


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


# Step 4: Main Function to scrape links and content
def scrape_dynamic_links_and_content(url):
    links = get_links_from_dynamic_page(url)
    # scraped_data = {}
    #
    # for link in links:
    #     print(f"Scraping content from: {link}")
    #     page_text = scrape_content_from_link(link)
    #     if page_text:
    #         scraped_data[link] = page_text
    #
    # return scraped_data
    return links


# Step 5: Example usage
if __name__ == "__main__":
    url_to_scrape = "https://www.codecademy.com/"  # Replace with your target URL
    scraped_links_and_content = (url_to_scrape)

    # Print out scraped content
    # for link, content in scraped_links_and_content.items():
    #     print(f"\nContent from {link}:\n{'-' * 40}\n{content}\n{'-' * 40}")

    print(get_links_from_dynamic_page(url_to_scrape))


def find_term_link(url, search_term="term"):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)

    # Set up the Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navigate to the page
        driver.get(url)

        # Wait for the page to load and find all links
        links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )

        # Search for a link containing the search term
        for link in links:
            href = link.get_attribute("href")
            if href and search_term.lower() in href.lower():
                return href


        return None  # If no matching link is found

    finally:
        driver.quit()


# Example usage
url = "https://www.codecademy.com/"
result = find_term_link(url)

if result:
    print(f"Found link containing 'term': {result}")
else:
    print("No link containing 'term' found")