pip install selenium
sudo apt update
sudo apt upgrade

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def create_browser():
    options = Options()
    options.headless = True  # run without opening a window
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(options=options)
    return browser

def login(email, password):
    browser = create_browser()
    browser.get("https://ucha.se/login/")

    time.sleep(2)  # wait for page to load

    try:
        # Find email and password input fields
        email_input = browser.find_element(By.NAME, "user[email]")
        password_input = browser.find_element(By.NAME, "user[password]")

        # Enter credentials
        email_input.send_keys(email)
        password_input.send_keys(password)

        # Submit login
        password_input.send_keys(Keys.RETURN)
        time.sleep(3)  # wait for login to process

        # Check login success
        if "logout" in browser.page_source.lower() or "изход" in browser.page_source.lower():
            print("Login successful!")
            return browser
        else:
            print("Login FAILED.")
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
        print("We are logged in and can continue...")
        # Example: navigate to a page after login
        browser.get("https://ucha.se/")
        time.sleep(2)
        print(browser.page_source[:500])  # first 500 chars of the page

        # Close browser when done
        browser.quit()
    else:
        print("Stopped.")

if __name__ == "__main__":
    main()
