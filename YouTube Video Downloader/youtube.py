from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# Creates a new driver and returns it
def create_driver():
    """
    Returns a new driver after each time it is called
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    return driver


# For logging into the LinkedIn account using the details given in the '.env' file 
def linkedin_login(driver):
    """
    For logging in, the '.env' file should look like this:
    export email="<your login email>"
    export password="<your login password>"
    """
    driver.get('https://linkedin.com/')

    time.sleep(3) # Let the user actually see something!

    email_input = driver.find_element(By.XPATH, '//input[@id="session_key" and @class="input__input"]')
    email_input.send_keys(os.environ.get('email'))

    password_input = driver.find_element(By.XPATH, '//input[@id="session_password" and @class="input__input"]')
    password_input.send_keys(os.environ.get('password'))

    password_input.submit()

    return None


driver = create_driver()

driver.get("https://www.youtube.com/watch?v=s-0DuYcWeBE")






driver.quit()