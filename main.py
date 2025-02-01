import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Path to cookies.json
COOKIES_PATH = "cookies.json"

# Start undetected Chrome
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

# 🚀 Block ads & make page load instantly
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")  # Disables all extensions (like ad scripts)
options.add_argument("--disable-popup-blocking")  # Stops popups
options.add_argument("--disable-infobars")  # Removes "Chrome is being controlled" banner
options.add_argument("--disable-blink-features=AutomationControlled")  # Anti-detection
options.add_argument("--blink-settings=imagesEnabled=false")  # Blocks images for faster load
options.add_argument("--disable-features=PreloadMediaEngagementData,MediaEngagementBypassAutoplayPolicies")  # Stops media autoplay
options.add_argument("--disable-site-isolation-trials")  # Prevents Chrome slowdowns
options.add_argument("--ignore-certificate-errors")  # Bypasses SSL errors

driver = uc.Chrome(options=options)

try:
    # Open Aternos login page
    driver.get("https://aternos.org/go")

    # Load saved cookies immediately
    with open(COOKIES_PATH, "r") as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

    # Refresh to apply cookies (should be logged in)
    driver.refresh()

    # ✅ Wait only for MHHS div (don't wait for full page)
    server_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@title='MHHS']"))
    )

    # Click MHHS div immediately when found
    actions = ActionChains(driver)
    actions.move_to_element(server_div).click().perform()
    print("✅ Entered the server!")

    # ✅ Wait only for the "Start" button to appear
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "start"))
    )

    # Click the "Start" button immediately
    actions.move_to_element(start_button).click().perform()
    print("✅ Start button clicked!")

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    driver.quit()
