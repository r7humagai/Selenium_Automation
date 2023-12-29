from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach", True)     # Leave the window open

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("http://www.neuralnine.com/")
driver.maximize_window()

# find all the links of the website,
# find all the anchor tags
links = driver.find_elements("xpath", "//a[@href]")     # atags with href attribute

for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break

book_links = driver.find_elements("xpath",
                                  "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a) = 2]//a")

for book_link in book_links:
    print(book_link.get_attribute("href"))

book_links[0].click()

driver.switch_to.window(driver.window_handles[1])

time.sleep(3)

buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(., '$')]]")

for button in buttons:
    print("Price Range:", button.get_attribute("innerHTML").replace('-', 'to'))