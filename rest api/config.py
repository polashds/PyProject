import os
from dotenv import load_dotenv

load_dotenv()

class APIConfig:
    BASE_URL = os.getenv("API_BASE_URL")
    KEY = os.getenv("API_KEY")
    TIMEOUT = int(os.getenv("API_TIMEOUT"))

    @classmethod
    def get_headers(cls):
        return {
            "Authorization" : f"Bearer {cls.KEY}",
            "Content-Type" : "application/json"
        }
    
