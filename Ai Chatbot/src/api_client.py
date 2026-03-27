from google import genai
from src.config import get_random_key

def get_client():
    key = get_random_key()
    return genai.Client(api_key=key)