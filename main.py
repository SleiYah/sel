import json
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ Start undetected Chrome (UC)
options = uc.ChromeOptions()

# 🚀 Disable headless mode for debugging (REMOVE `#` WHEN DEPLOYING)
# options.add_argument("--headless=new")

options.add_argument("--start-maximized")  # ✅ Open Chrome full screen
options.add_argument("--disable-gpu")  # ✅ Fix rendering issues
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# ✅ Start WebDriver with UC
driver = uc.Chrome(options=options)

try:
    print("🌐 Opening Aternos website...")
    driver.get("https://aternos.org/go")

    # ✅ Load saved cookies
    print("🔑 Loading cookies...")
    with open("cookies.json", "r") as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

    # ✅ Refresh to apply cookies
    driver.refresh()
    print("✅ Cookies applied! Logged in successfully.")

    # ✅ Ensure the page is fully loaded before searching for elements
    print("⏳ Waiting for page to load completely...")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # ✅ Wait for the server list container
    print("🕵️‍♂️ Looking for the server list container...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "servercardlist"))
    )

    # ✅ Find the server using class name
    print("🕵️‍♂️ Searching for MHHS server by class name...")
    server_div = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".servercard.offline"))  # 🔥 Use CSS Selector for classes
    )

    print("✅ Found MHHS server! Clicking it...")
    actions = ActionChains(driver)
    actions.move_to_element(server_div).click().perform()

    # ✅ Wait for the "Start" button
    print("🕵️‍♂️ Looking for the 'Start' button...")
    start_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "start"))
    )

    # ✅ Click the "Start" button
    actions.move_to_element(start_button).click().perform()
    print("✅ Start button clicked! 🚀")

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    print("🛑 Closing browser...")
    driver.quit()
