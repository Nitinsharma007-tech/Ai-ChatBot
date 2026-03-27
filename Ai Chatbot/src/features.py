from src.api_client import get_client
from src.config import MODEL_ID

# 📘 Explain Text
def explain_text(prompt):
    client = get_client()

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )

    return response.text


# 🖼️ Image Analysis
def analyze_image(image):
    client = get_client()

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=["Explain this image", image]
    )

    return response.text


# 💬 Chat Streaming
def chat_stream(prompt):
    client = get_client()

    stream = client.models.generate_content_stream(
        model=MODEL_ID,
        contents=prompt
    )

    for chunk in stream:
        if chunk.text:
            yield chunk.text