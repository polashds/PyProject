# demo_request.py
import requests
from config import APIConfig
import logging

# =============================
# Configure Logging
# =============================
logging.basicConfig(
    level=logging.INFO,  # Use DEBUG for more verbose logs
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("api_demo.log", mode="a", encoding="utf-8"),  # log to file
        logging.StreamHandler()  # also print to console
    ]
)

logger = logging.getLogger(__name__)


# =============================
# GET Request
# =============================
def safe_get_users():
    url = f"{APIConfig.BASE_URL}/users"
    logger.info("Starting GET request to %s", url)

    try:
        response = requests.get(
            url,
            headers=APIConfig.get_headers(),
            timeout=APIConfig.TIMEOUT
        )

        logger.debug("Raw GET response: %s", response.text)
        response.raise_for_status()

        users = response.json()
        if users:
            print("✅ GET successful. First user:", users[0])
            logger.info("✅ GET successful. First user: %s", users[0])
        else:
            logger.warning("GET successful but no users returned.")

    except requests.exceptions.Timeout:
        logger.error("⏱️ Request timed out for GET /users")

    except requests.exceptions.ConnectionError:
        logger.error("❌ Connection error during GET /users")

    except requests.exceptions.HTTPError as e:
        logger.error("📡 HTTP error during GET /users: %s", e)

    except Exception as e:
        logger.exception("Unexpected error during GET /users: %s", e)


# =============================
# POST Request
# =============================
def safe_posts():
    url = f"{APIConfig.BASE_URL}/posts"
    logger.info("Starting POST request to %s", url)

    new_post = {
        "title": "Hello API World",
        "body": "This is a demo post from Python requests.",
        "userId": 1
    }

    logger.debug("Payload for POST: %s", new_post)

    try:
        response_post = requests.post(
            url,
            headers=APIConfig.get_headers(),
            json=new_post,
            timeout=APIConfig.TIMEOUT
        )

        logger.debug("Raw POST response: %s", response_post.text)
        response_post.raise_for_status()

        post_data = response_post.json()
        print("✅ POST successful. New post:", post_data)
        logger.info("✅ POST successful. New post response: %s", post_data)

    except requests.exceptions.Timeout:
        logger.error("⏱️ Request timed out for POST /posts")

    except requests.exceptions.ConnectionError:
        logger.error("❌ Connection error during POST /posts")

    except requests.exceptions.HTTPError as e:
        logger.error("📡 HTTP error during POST /posts: %s", e)

    except Exception as e:
        logger.exception("Unexpected error during POST /posts: %s", e)


# =============================
# Main Entry Point
# =============================
if __name__ == "__main__":
    logger.info("=== Starting demo_request.py ===")

    print("=== GET /users ===")
    safe_get_users()

    print("\n=== POST /posts ===")
    safe_posts()

    logger.info("=== Script completed ===")
