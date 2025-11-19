from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def open_edge_with_profile():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    # reuse existing Edge login profile:
    options.add_argument(r"user-data-dir=%LOCALAPPDATA%\Microsoft\Edge\User Data")
    options.add_argument("--profile-directory=Default")

    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options
    )
    return driver

driver = open_edge_with_profile()

# 1. Open your dashboard
driver.get("YOUR_DASHBOARD_URL_HERE")
time.sleep(4)   # wait for highcharts to render

# 2. Click the Decommission → New cell (text changes daily)
xpath = "//path[contains(@aria-label, 'New Decommission')]"

cell = driver.find_element(By.XPATH, xpath)
driver.execute_script("arguments[0].scrollIntoView({block:'center'})", cell)
time.sleep(0.5)
cell.click()

print("SUCCESS: Clicked the Decommission → New cell.")
