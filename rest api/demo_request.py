# demo_request.py
import requests
from config import APIConfig

# === GET request ===
print("=== GET /users ===")
def safe_get_users():
    try:
        response = requests.get(
            f"{APIConfig.BASE_URL}/users",
            headers=APIConfig.get_headers(),
            timeout=APIConfig.TIMEOUT
        )

        print("Status Code:", response.status_code)
        print("First user:", response.json()[0])  # show first user

        response.raise_for_status()
        users = response.json()
        print("✅ GET successful. First user:", users[0])

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Connection error.")
    except requests.exceptions.HTTPError:
        print("HTTP error.")
    except Exception as e:
        print(f"An error occurred: {e}")

# === POST request ===
print("\n=== POST /posts ===")

def safe_posts():
    try:
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

        response_post.raise_for_status()
        print("✅ POST successful. New post:", response_post.json())

        response_post.raise_for_status()

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Connection error.")
    except requests.exceptions.HTTPError:
        print("HTTP error.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":  # only run if this file is executed directly
    print("=== GET /users ===")
    safe_get_users()

    print("\n=== POST /posts ===")
    safe_posts()