import requests
from config import APIConfig

# Send GET request to public API
response = requests.get(
    f"{APIConfig.BASE_URL}/users",   # becomes https://jsonplaceholder.typicode.com/users
    headers=APIConfig.get_headers(),
    timeout=APIConfig.TIMEOUT
)

# Print results
print("Status Code:", response.status_code)  # should be 200
print("Response JSON (first user):")
print(response.json()[0])  # show first user