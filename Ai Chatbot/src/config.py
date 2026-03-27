import random

# 🔑 Add your keys here
API_KEYS = [
    "AIzaSyDlFBMBx2D-kyStW5sesk1T1bcXHLmBoag",
    "AIzaSyClwhD8NbR3my0ZfNb347my7g0nVGwbDdA",
    "AIzaSyCVlM_Upyz1qnkAx0_8qsy1ceBcx6MY5ak",
    "AIzaSyAKNx_8EmZkVdvXVtBKskCVVsXDCv5WKDU",
    "AIzaSyAPXf7-2kgixi0V7RfAo2ePKG7X8e-57P0"
]

MODEL_ID = "gemini-3-flash-preview"

def get_random_key():
    return random.choice(API_KEYS)