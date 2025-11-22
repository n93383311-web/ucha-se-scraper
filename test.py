import requests

url = "https://ucha.se/users/sign_in"
r = requests.get(url)
print(r.status_code)
print(r.text[:500])
