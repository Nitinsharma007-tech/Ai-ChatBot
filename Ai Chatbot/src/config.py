import random

# 🔑 Add your keys here
API_KEYS = [
    
]

MODEL_ID = "gemini-3-flash-preview"

def get_random_key():
    return random.choice(API_KEYS)
