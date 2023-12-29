'''
This Selenium script automates the extraction of book links and corresponding paperback price ranges from the 'neuralnine.com'.
It navigates to the site, filters book links based on specific criteria, and prints the resulting href attributes and associated price ranges.
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

'''
# Configure Chrome options
This sets up the chrome options, including the experimental option to detach the browser(leave it open after the script finishes.)
'''
options = Options()
options.add_experimental_option("detach", True)     # Leave the window open

'''
# Initialize Chrome WebDriver
Uses Selenium to initialize the Chrome WebDriver, specifying the ChromeDriver executable through 'ChromeDriverManager()'.
'''

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# Open the website and maximize the window
driver.get("http://www.neuralnine.com/")
driver.maximize_window()

# find all the links of the website (all anchor tags with an href attribute)
links = driver.find_elements("xpath", "//a[@href]")

# Iterate through links and click on the one containing "Books" in its inner HTML
'''
This finds all links on the page and click on the one whose innerHTML contains "Books".
'''
for link in links:
    if "Books" in link.get_attribute("innerHTML"):
        link.click()
        break

# -> Xpath(XML Path Language) is a query language used to navigate and select elements in XML & HTML Documents.
#    It provides a way to locate and traverse elements in an XML or HTML tree structure by defining paths.

# Finds book links based on specific criteria using XPath
'''
This uses xpath to find book links based on specific criteria
(eg. elements with certain class,
     containing a specific heading,
     and having a certain number of anchor tags).
'''
book_links = driver.find_elements("xpath",
                                  "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a) = 2]//a")

# Prints the href attribute of each book link
for book_link in book_links:
    print(book_link.get_attribute("href"))

# Clicks on the first book link
book_links[0].click()

# Switch to the new tab/window
driver.switch_to.window(driver.window_handles[1])

# Optional delay timer for the new page to load.
time.sleep(3)

# Finds buttons containing the price information using XPath
# Uses Xpath to find buttons containing price information
buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(., 'Paperback')]]]//span[text()[contains(., '$')]]")

# Print the price range for each button.
for button in buttons:
    print("Price Range:", button.get_attribute("innerHTML").replace('-', 'to'))