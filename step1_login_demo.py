# step1_login_demo.py
import requests

url = "http://192.168.168.64:48080/admin-api/system/auth/login"

payload = {
    "username": "0366",
    "password": "1111D"
}

headers = {
    "Content-Type": "application/json",
    "tenant-id": "1"
}

response = requests.post(url, json=payload, headers=headers)

print(response.status_code)
print(response.text)
print(response.json())