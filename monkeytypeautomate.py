from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--enable-unsafe-swiftshader')
chrome_options.add_argument('--disable-plugins')
chrome_options.add_argument('--disable-web-security')
chrome_options.add_argument('--disable-features=WebRTC')
chrome_options.add_argument('--disable-software-rasterizer')
chrome_options.add_argument('--disable-compositing')
chrome_options.add_argument('--disable-rtc')
# chrome_options.add_argument('--headless')
chrome_options.add_experimental_option("detach", True)  
chrome_options.add_argument('--log-level=3')  # Suppresses warnings and errors

chrome_options.add_argument("--disable-blink-features=AutomationControlled")
service = Service()
browser=webdriver.Chrome(options=chrome_options,service=service)
browser.get("https://monkeytype.com")
try:
   browser.execute_script('document.getElementsByClassName("acceptAll")[0].click();')
except Exception:
    pass

words = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.ID, "words"))
)
print(words.text, "words")
browser.find_element(By.CSS_SELECTOR, ".word.active").click()

try:
    while len(browser.find_elements(By.CLASS_NAME, "word")) != 0:
     ActionChains(browser).send_keys([letter.text for letter in browser.find_element(By.CSS_SELECTOR, ".word.active").find_elements(By.TAG_NAME, "letter")] + [' ']).perform()
     time.sleep(0.13)
except Exception as e:
        print(e)

