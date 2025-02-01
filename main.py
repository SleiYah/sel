import os
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from webdriver_manager.chrome import ChromeDriverManager

# ✅ Let webdriver-manager install and manage ChromeDriver automatically
options = uc.ChromeOptions()
options.add_argument("--headless=new")  # ✅ Headless mode for Railway
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# ✅ Initialize WebDriver without manually setting a path
service = Service(ChromeDriverManager().install())
driver = uc.Chrome(service=service, options=options)

try:
    print("🌐 Opening Aternos website...")
    driver.get("https://aternos.org/go")

    # ✅ Load saved cookies
    print("🔑 Loading cookies...")
    with open("cookies.json", "r") as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

    # ✅ Refresh to apply cookies (should be logged in)
    driver.refresh()
    print("✅ Cookies applied! Logged in successfully.")

    # ✅ Wait for MHHS div (no full page wait)
    print("🕵️‍♂️ Looking for your server (MHHS)...")
    server_div = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@title='MHHS']"))
    )

    # Click MHHS div immediately when found
    actions = ActionChains(driver)
    actions.move_to_element(server_div).click().perform()
    print("✅ Entered the server!")

    # ✅ Wait for the "Start" button to appear
    print("🕵️‍♂️ Looking for the 'Start' button...")
    start_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, "start"))
    )

    # Click the "Start" button immediately
    actions.move_to_element(start_button).click().perform()
    print("✅ Start button clicked! 🚀")

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    print("🛑 Closing browser...")
    driver.quit()
