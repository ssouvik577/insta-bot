# ================Imports necessary modules and libraries================
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# =======================================================================

# Sets up the Chrome browser options to maximize the window and not close the browser automatically when the script finishes.
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
# ========================================================================

# Navigates to the Instagram website
url = "https://www.instagram.com/"
driver.get(url)
time.sleep(3)

# Enters the login credentials (username and password) into the respective input fields
username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys("internetpoint621@gmail.com")
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys("Tupai@123")

# Logs in by sending the ENTER key press on the password input field
password.send_keys(Keys.ENTER)
time.sleep(5)

# Clicks on the "Not Now" button when asked to save login information
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
time.sleep(3)

# Navigates to a user's Instagram profile page by using the search bar and entering the username
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div').click()
search = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
time.sleep(2)

# Clicks on the user's profile to open it.
search.send_keys("bhuvan.bam22")
time.sleep(3)

# Opens the user's first post by clicking on it
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a').click()
time.sleep(3)

# Clicks on the "Like" button of the first post to like it
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a').click()
time.sleep(1)

driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button').click()
time.sleep(1)

# Scrolls through the next 10 posts and likes each of them using for loop
for i in range(2,11):
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button').click()  #Next Button

