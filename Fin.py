from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import os

# Start Edge with your existing login cookies
def open_edge_with_profile():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    # This loads your already-logged-in Microsoft Edge profile
    options.add_argument(fr"user-data-dir={os.path.expandvars('%LOCALAPPDATA%')}\Microsoft\Edge\User Data")
    options.add_argument("--profile-directory=Default")
    return webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options
    )

# 1. Open browser
driver = open_edge_with_profile()

# 2. Open your dashboard URL
driver.get("PASTE_YOUR_DASHBOARD_URL_HERE")
time.sleep(4)  # allow highcharts to render

# 3. XPATH for "Decommission → New" cell
xpath = "//path[contains(@aria-label, 'New Decommission')]"

# 4. Try to click
cell = driver.find_element(By.XPATH, xpath)
driver.execute_script("arguments[0].scrollIntoView({block:'center'})", cell)
time.sleep(1)
cell.click()

print("SUCCESS: CLICK PERFORMED")
