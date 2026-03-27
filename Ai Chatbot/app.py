import streamlit as st
from src.prompts import apply_mode
from src.features import chat_stream, explain_text, analyze_image
from PIL import Image

st.set_page_config(page_title="BharatAI Chatbot", layout="wide")

st.title("🇮🇳 BharatAI - AI Chatbot")

# 🧠 Sidebar
mode = st.sidebar.radio("Select Mode", ["Normal", "Student", "Business"])

# 🎯 Feature selector
feature = st.selectbox(
    "What do you want to do?",
    ["Chat", "Explain Text", "Analyze Image"]
)

# =========================
# 💬 CHAT
# =========================
if feature == "Chat":

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask something...")

    if user_input:

        prompt = apply_mode(user_input, mode)

        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_response = ""

            for chunk in chat_stream(prompt):
                full_response += chunk
                placeholder.markdown(full_response + "▌")

            placeholder.markdown(full_response)

        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )

# =========================
# 📘 EXPLAIN TEXT
# =========================
elif feature == "Explain Text":

    text = st.text_area("Enter text")

    if st.button("Explain"):

        prompt = apply_mode(text, mode)
        result = explain_text(prompt)

        st.write(result)

# =========================
# 🖼️ IMAGE ANALYSIS
# =========================
elif feature == "Analyze Image":

    file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

    if file:
        image = Image.open(file)
        st.image(image)

        if st.button("Analyze"):
            result = analyze_image(image)
            st.write(result)