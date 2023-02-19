# <----- Modules Imported ----->
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# <----- Launches Web Drivers & Visit's To WhatsApp Web ----->
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# <----- After Scanning For Login Page Press Enter ----->
input("Press Enter after scanning the QR code")

# <----- Find The Group Where You Want To Send/Spam Message ----->
contact = driver.find_element_by_xpath("//span[@title='Contact or Group Name']")
contact.click()

# <----- Navigate Through Message Send Field ----->
input_box = driver.find_element_by_xpath("//div[@class='_2_1wd copyable-text selectable-text']")
input_box.send_keys("Hello, this is a test message" + Keys.ENTER)

# <----- Closes Down The Selenium Drive ----->
time.sleep(5)
driver.close()

# <----- Make Sure To Star The Repo ----->
