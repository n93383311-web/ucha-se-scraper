from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def create_browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Use Google Chrome
    options.binary_location = "/usr/bin/google-chrome"

    # Use installed chromedriver
    service = Service("/usr/local/bin/chromedriver")

    browser = webdriver.Chrome(service=service, options=options)
    return browser

def login(email, password):
    browser = create_browser()
    browser.get("https://ucha.se/login/")
    time.sleep(2)

    try:
        email_input = browser.find_element(By.NAME, "user[email]")
        password_input = browser.find_element(By.NAME, "user[password]")

        email_input.send_keys(email)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        time.sleep(3)

        if "изход" in browser.page_source.lower() or "logout" in browser.page_source.lower():
            print("Login successful!")
            return browser
        else:
            print("Login failed.")
            browser.quit()
            return None

    except Exception as e:
        print("Error during login:", e)
        browser.quit()
        return None

def main():
    email = input("Email: ")
    password = input("Password: ")

    browser = login(email, password)
    if browser:
        print("Logged in! Going to homepage...")
        browser.get("https://ucha.se/")
        time.sleep(2)
        print(browser.page_source[:200])
        browser.quit()
    else:
        print("Stopped.")

if __name__ == "__main__":
    main()
