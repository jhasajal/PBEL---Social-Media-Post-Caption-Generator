import streamlit as st
from modules.voice_input import transcribe_voice
from modules.image_caption import caption_from_image
from modules.prompt_builder import build_prompt
from modules.langgraph_runner import generate_caption
import os
import datetime

# History storage file
HISTORY_FILE = "history.txt"

st.set_page_config(page_title="Social Media Caption Generator", layout="centered")
st.title("🎯 Social Media Post & Caption Generator")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Text and voice input logic
st.subheader("📝 Enter Theme or Topic")
input_method = st.radio("Choose input method:", ["Text", "Voice"], horizontal=True)

# --- 1. If Text is selected
if input_method == "Text":
    typed_input = st.text_input("Type your theme or keywords:")
    if typed_input:
        st.session_state["user_input"] = typed_input
        st.session_state["transcription"] = ""

# --- 2. If Voice is selected
elif input_method == "Voice":
    if st.button("🎤 Record Voice"):
        voice_input = transcribe_voice()
        if voice_input:
            st.session_state["user_input"] = voice_input
            st.session_state["transcription"] = voice_input
            st.rerun()

# Get user input
user_input = st.session_state.get("user_input", "")
transcription = st.session_state.get("transcription", "")

# Show transcription if any
if transcription:
    st.markdown(f"🗣️ **Transcribed Text:** _{transcription}_")

# Optional image
st.subheader("🖼️ Upload an Image (optional)")
image_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

# --- Configuration Section ---
st.subheader("🎭 Choose Tone & Platform")
tone = st.selectbox("Tone", ["Casual", "Funny", "Formal", "Inspirational", "Witty"])
platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "Twitter"])

# --- Generate Caption ---
if st.button("⚡ Generate Caption"):
    with st.spinner("Generating..."):
        final_input = user_input

        if not final_input and image_file:
            final_input = caption_from_image(image_file)

        if not final_input:
            st.error("Please provide text input or upload an image.")
        else:
            prompt = build_prompt(final_input, tone, platform)
            caption = generate_caption(prompt)

            st.subheader("📄 Generated Caption")
            st.text_area("Your Caption", caption, height=100)

            # Save to local history
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"[{timestamp}] ({platform} | {tone})\n{caption}\n\n"
            with open(HISTORY_FILE, "a") as f:
                f.write(entry)

            st.session_state.history.insert(0, entry)

# --- History Section ---
st.subheader("📜 History")
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        history = f.read().strip().split("\n\n")[-10:] 
        for item in reversed(history):
            st.markdown(f"```\n{item}\n```")
else:
    st.info("No history yet.")
