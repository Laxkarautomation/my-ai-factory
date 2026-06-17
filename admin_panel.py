import streamlit as st
import requests

# Yahan wahi URL dalna jo ngrok se milega
GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev/"

st.set_page_config(page_title="AI Factory Control Tower", layout="wide")
st.title("🚀 AI Factory Control Tower")

st.subheader("1. Asset Upload")
uploaded_video = st.file_uploader("Upload Video", type=['mp4'])
uploaded_image = st.file_uploader("Upload Photo", type=['jpg', 'png'])

if st.button("Upload to GPU"):
    if uploaded_video and uploaded_image:
        files = {"video": uploaded_video, "image": uploaded_image}
        try:
            # Upload URL same port par bhej rahe hain
            res = requests.post(f"{GPU_SERVER_URL}/upload", files=files, timeout=60)
            if res.status_code == 200: st.success("Upload Successful!")
            else: st.error(f"Upload Failed: {res.status_code}")
        except Exception as e: st.error(f"Connection Error: {e}")

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
        if res.status_code == 200: st.success("Transformation queued!")
        else: st.error("Server Error.")
    except Exception as e: st.error(f"Connection Failed: {e}")
