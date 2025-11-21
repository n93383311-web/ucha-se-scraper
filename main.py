import requests

LOGIN_URL = "https://ucha.se/users/sign_in"

def login(email, password):
    session = requests.Session()

    # Visit login page to get authenticity_token
    r = session.get(LOGIN_URL)
    if r.status_code != 200:
        print("Could not load login page.")
        return None

    # extract authenticity_token
    import re
    token_match = re.search(r'name="authenticity_token" value="([^"]+)"', r.text)
    if not token_match:
        print("Could not find authenticity_token.")
        return None

    token = token_match.group(1)

    payload = {
        "user[email]": email,
        "user[password]": password,
        "authenticity_token": token
    }

    # send login form
    r2 = session.post(LOGIN_URL, data=payload)

    # check login success
    if "logout" in r2.text.lower() or "изход" in r2.text.lower():
        print("Login success!")
        return session
    else:
        print("Login FAILED.")
        return None


def main():
    email = input("Email: ")
    password = input("Password: ")

    session = login(email, password)
    if session:
        print("We are logged in and can continue...")
    else:
        print("Stopped.")


if __name__ == "__main__":
    main()
