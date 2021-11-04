from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = getenv("API_ID")
API_HASH =getenv("API_HASH")
TOKEN =getenv("TOKEN")
SUDO = list(map(int, getenv("SUDO").split()))