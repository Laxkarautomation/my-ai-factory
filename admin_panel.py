import streamlit as st
import requests

# Yahan apna Ngrok URL daalo
GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev/"

st.set_page_config(layout="wide")
st.title("🚀 AI Content Factory")

st.subheader("1. Upload Assets")
uploaded_video = st.file_uploader("Upload Video", type=['mp4'])
uploaded_image = st.file_uploader("Upload Photo", type=['jpg', 'png'])

if st.button("Upload to GPU"):
    if uploaded_video and uploaded_image:
        files = {"video": uploaded_video, "image": uploaded_image}
        try:
            res = requests.post(f"{GPU_SERVER_URL}/upload", files=files, timeout=60)
            if res.status_code == 200: st.success("Upload Successful!")
            else: st.error(f"Error: {res.status_code}")
        except Exception as e: st.error(f"Conn Error: {e}")

st.subheader("2. Run Transformation")
if st.button("Run Viral Transformation"):
    payload = {
        "prompt": {
            "1": {"inputs": {"image": "avatar.jpg"}, "class_type": "LoadImage"},
            "2": {"inputs": {"filename_prefix": "Viral", "images": ["1", 0]}, "class_type": "SaveImage"}
        }
    }
    try:
        res = requests.post(f"{GPU_SERVER_URL}/prompt", json=payload, timeout=60)
        if res.status_code == 200: st.success("Queued!")
        else: st.error("Server Error")
    except Exception as e: st.error(f"Conn Error: {e}")
