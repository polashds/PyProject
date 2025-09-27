import aiofiles
import asyncio
import logging
from pathlib import Path



# Define your parent dir once
BASE_DIR = Path(r"e:\Py-Projects-Vault\PyProject\asynchronous")

# LOG FILE ADDED
LOG_FILE = BASE_DIR / "fileio.log"

# configure logging to both file and console
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8"), # write logs to file
        logging.StreamHandler() # also print to console
    ]
)


async def read_file_async(filename):
    filepath = BASE_DIR / filename
    logging.info(f"Reading file: {filepath}")
    try:
        async with aiofiles.open(filepath, 'r', encoding='utf-8') as f:
            content = await f.read()
            logging.info(f"Succefully read file: {filepath}")
            return content
    
    except FileNotFoundError as e:
        logging.error(f"File not found: {filepath}")
        return ""
    except Exception as e:
        logging.exception(f"An error occurred while reading file: {filepath}: {e}")
        return ""   
async def main():
    logging.info("proram started")
    content = await read_file_async("dummy_dataset.csv")
    print(content)

    if content:
        logging.info("File content successfully retrieved")
        print(content)
    else:
        logging.warning("No content to display (file missing or empty)")

    logging.info("Program finished")

if __name__ == "__main__":
    asyncio.run(main())