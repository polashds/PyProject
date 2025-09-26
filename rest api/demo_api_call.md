Perfect 👍 let’s make a **runnable demo** using a free public API so you can test everything yourself.

We’ll use 👉 **[JSONPlaceholder](https://jsonplaceholder.typicode.com/)**, a free fake REST API for testing.

---

## 🟢 Step 1: Create `.env` file

In your project folder, create a file named `.env` with this content:

```ini
API_BASE_URL=https://jsonplaceholder.typicode.com
API_KEY=demo123   # not actually used here, but kept for demo
API_TIMEOUT=10
```

---

## 🟢 Step 2: Create `config.py`

```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # load .env file

class APIConfig:
    BASE_URL = os.getenv('API_BASE_URL')
    KEY = os.getenv('API_KEY')
    TIMEOUT = int(os.getenv('API_TIMEOUT', 30))  # default 30 sec
    
    @classmethod
    def get_headers(cls):
        return {
            "Authorization": f"Bearer {cls.KEY}",
            "Content-Type": "application/json"
        }
```

---

## 🟢 Step 3: Create `demo_request.py`

```python
# demo_request.py
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
```

---

## 🟢 Step 4: Run it

In terminal:

```bash
python demo_request.py
```

---

## ✅ Expected Output

Something like:

```
Status Code: 200
Response JSON (first user):
{'id': 1,
 'name': 'Leanne Graham',
 'username': 'Bret',
 'email': 'Sincere@april.biz',
 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556',
             'city': 'Gwenborough', 'zipcode': '92998-3874',
             'geo': {'lat': '-37.3159', 'lng': '81.1496'}},
 'phone': '1-770-736-8031 x56442',
 'website': 'hildegard.org',
 'company': {'name': 'Romaguera-Crona',
             'catchPhrase': 'Multi-layered client-server neural-net',
             'bs': 'harness real-time e-markets'}}
```

---

👉 That’s a **real API request** using your config setup.




Great 👍 let’s extend the demo to include a **POST request** so you can see how to **send data to an API**.

We’ll still use **[JSONPlaceholder](https://jsonplaceholder.typicode.com/)** because it accepts fake POST requests (it won’t really save data, but it will pretend to and send back a response).

---

## 🟢 Step 1: Add a POST example in `demo_request.py`

```python
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
```

---

## 🟢 Step 2: Run it

```bash
python demo_request.py
```

---

## ✅ Expected Output

```
=== GET /users ===
Status Code: 200
First user: {'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', ...}

=== POST /posts ===
Status Code: 201
Response JSON: {'title': 'Hello API World',
                'body': 'This is a demo post from Python requests.',
                'userId': 1,
                'id': 101}
```

---

### 🟢 What’s happening in the POST?

* `requests.post(...)` sends data to the API.
* `json=new_post` automatically converts the Python dictionary into JSON (like `{"title": "...", "body": "...", "userId": 1}`).
* Server replies with a fake new record including an `id`.

---

⚡ Analogy:

* GET = reading from a library 📖
* POST = adding a new book to the library 📚

---

Perfect 👍 error handling is super important because APIs can fail, be slow, or reject requests. Let’s add **try/except** blocks so your code is safe.

We’ll expand `demo_request.py` to handle errors for both **GET** and **POST**.

---

## 🟢 Updated `demo_request.py` with Error Handling

```python
# demo_request.py
import requests
from config import APIConfig

def safe_get_users():
    """GET request with error handling"""
    try:
        response = requests.get(
            f"{APIConfig.BASE_URL}/users",
            headers=APIConfig.get_headers(),
            timeout=APIConfig.TIMEOUT
        )
        response.raise_for_status()  # raise error if status code is 4xx/5xx
        users = response.json()
        print("✅ GET successful. First user:", users[0])
    except requests.exceptions.Timeout:
        print("⏳ Request timed out!")
    except requests.exceptions.ConnectionError:
        print("❌ Failed to connect to the API.")
    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP error occurred: {e}")
    except Exception as e:
        print(f"🔥 Unexpected error: {e}")


def safe_post():
    """POST request with error handling"""
    new_post = {
        "title": "Hello API World",
        "body": "This is a demo post from Python requests.",
        "userId": 1
    }

    try:
        response = requests.post(
            f"{APIConfig.BASE_URL}/posts",
            headers=APIConfig.get_headers(),
            json=new_post,
            timeout=APIConfig.TIMEOUT
        )
        response.raise_for_status()
        print("✅ POST successful. Response JSON:", response.json())
    except requests.exceptions.Timeout:
        print("⏳ POST request timed out!")
    except requests.exceptions.ConnectionError:
        print("❌ Failed to connect to the API.")
    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP error occurred: {e}")
    except Exception as e:
        print(f"🔥 Unexpected error: {e}")


if __name__ == "__main__":
    print("=== Running GET ===")
    safe_get_users()

    print("\n=== Running POST ===")
    safe_post()
```

---

## 🟢 What changed?

1. **`try/except` around requests**

   * Catches errors instead of letting the program crash.

2. **`response.raise_for_status()`**

   * If API returns `404 Not Found` or `500 Server Error`, this will raise an exception you can catch.

3. **Error types handled**

   * `Timeout` → server too slow.
   * `ConnectionError` → server not reachable.
   * `HTTPError` → server responded with 4xx/5xx.
   * `Exception` → catches anything else unexpected.

---

## 🟢 Example Scenarios

* If API works ✅:

  ```
  === Running GET ===
  ✅ GET successful. First user: {'id': 1, 'name': 'Leanne Graham', ...}

  === Running POST ===
  ✅ POST successful. Response JSON: {'title': 'Hello API World', ...}
  ```

* If API URL is wrong ❌ (`API_BASE_URL=wrong-url`):

  ```
  ❌ Failed to connect to the API.
  ```

* If server takes too long ⏳:

  ```
  ⏳ Request timed out!
  ```

---

⚡ With this setup, your script **never crashes**—it gives clear messages about what went wrong.



Perfect! Let’s go step by step on **how to write unit tests for your API functions** using **pytest** and **mocking**, so you can test without hitting the real API.

We’ll use Python’s `unittest.mock` to simulate API responses.

---

## 🟢 Step 1: Install pytest (if not installed)

```bash
pip install pytest
```

---

## 🟢 Step 2: Create a test file `test_demo_request.py`

```python
# test_demo_request.py
import pytest
from unittest.mock import patch, Mock
from demo_request import safe_get_users, safe_post

# ----------------- TEST GET -----------------
@patch("demo_request.requests.get")
def test_safe_get_users_success(mock_get):
    # Create a fake response object
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "name": "Test User"}]
    mock_response.raise_for_status.return_value = None

    mock_get.return_value = mock_response

    safe_get_users()  # call function, should print first user

# ----------------- TEST POST -----------------
@patch("demo_request.requests.post")
def test_safe_post_success(mock_post):
    # Create a fake response object
    mock_response = Mock()
    mock_response.status_code = 201
    mock_response.json.return_value = {
        "title": "Hello API World",
        "body": "This is a demo post from Python requests.",
        "userId": 1,
        "id": 101
    }
    mock_response.raise_for_status.return_value = None

    mock_post.return_value = mock_response

    safe_post()  # call function, should print response JSON
```

---

## 🟢 Step 3: How it works

1. **`@patch("demo_request.requests.get")`**

   * Replaces `requests.get` with a fake object (`mock_get`).
   * No real network call happens.

2. **`mock_response = Mock()`**

   * Create a fake response object.
   * Set properties like `status_code` and `json.return_value` to mimic a real API response.

3. **`mock_get.return_value = mock_response`**

   * When `safe_get_users()` calls `requests.get`, it receives the fake response.

4. **Same concept for POST request**.

---

## 🟢 Step 4: Run tests

```bash
pytest -v test_demo_request.py
```

Expected output:

```
test_demo_request.py::test_safe_get_users_success PASSED
test_demo_request.py::test_safe_post_success PASSED
```

✅ Both tests pass without hitting the real API.

---

### 🟢 Why this is useful

* You can **test API logic safely** even if:

  * The real API is slow.
  * You don’t want to use your API key repeatedly.
  * The API has usage limits.

* You can simulate **success, failure, timeout, or server errors** by adjusting `mock_response`.

---

If you want, I can make an **enhanced version** where we also **test error handling** (timeouts, 404 errors, etc.) with mocking—so you can fully test your `safe_get_users()` and `safe_post()` functions.

Do you want me to do that next?
