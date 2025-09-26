# demo_request.py
import requests
from config import APIConfig

# === GET request ===
print("=== GET /users ===")
response = requests.get(
    f"{APIConfig.BASE_URL}/users",
    headers=APIConfig.get_headers(),
    timeout=APIConfig.TIMEOUT
)

print("Status Code:", response.status_code)
print("First user:", response.json()[0])  # show first user


# === POST request ===
print("\n=== POST /posts ===")
new_post = {
    "title": "Hello API World",
    "body": "This is a demo post from Python requests.",
    "userId": 1
}

response_post = requests.post(
    f"{APIConfig.BASE_URL}/posts",
    headers=APIConfig.get_headers(),
    json=new_post,  # send data as JSON
    timeout=APIConfig.TIMEOUT
)

print("Status Code:", response_post.status_code)  # usually 201
print("Response JSON:", response_post.json())
