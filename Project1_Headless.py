# Headless for Project1_Basic: Add argument in Options

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")
options.add_argument('--window-size = 300, 300')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://www.neuralnine.com/")
driver.maximize_window()

links = driver.find_elements("xpath", "//a[@href]")

for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        #link.click()
        driver.execute_script('arguments[0].click();', link)
        break

book_links = driver.find_elements("xpath",
                                  "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a) = 2]//a")

for book_link in book_links:
    print(book_link.get_attribute("href"))

driver.execute_script("arguments[0].click();", book_links[0])
#book_links[0].click()

driver.switch_to.window(driver.window_handles[1])
time.sleep(3)

buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(., '$')]]")

# Wait for the buttons to be visible
print("Number of buttons: ", len(buttons))

for button in buttons:
    print("Price Range:", button.get_attribute("innerHTML").replace('-', 'to'))