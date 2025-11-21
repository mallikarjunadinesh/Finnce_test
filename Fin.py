from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os, time

# 🔹 START EDGE WITH YOUR LOGGED-IN PROFILE
def start_edge():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    options.add_argument(fr"user-data-dir={os.path.expandvars('%LOCALAPPDATA%')}\Microsoft\Edge\User Data")
    options.add_argument("--profile-directory=Default")
    service = Service(EdgeChromiumDriverManager().install())   # AUTO DRIVER DOWNLOAD
    return webdriver.Edge(service=service, options=options)

# 🔹 REPLACE WITH YOUR DASHBOARD URL
DASHBOARD_URL = "PASTE_YOUR_DASHBOARD_URL_HERE"

driver = start_edge()
driver.get(DASHBOARD_URL)

time.sleep(5)   # Wait for dashboard + chart to load

# 🔹 This finds the cell with dynamic number (20 / 18 / etc)
xpath = "//path[contains(@aria-label, 'New Decommission')]"

elem = driver.find_element(By.XPATH, xpath)
driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
time.sleep(1)
elem.click()

print("CLICKED SUCCESSFULLY!")
