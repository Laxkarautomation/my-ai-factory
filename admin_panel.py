import streamlit as st
import requests

# Ngrok ka wahi URL dalo jo tunnel se mila hai
GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev/"

st.set_page_config(layout="wide")
st.title("🚀 AI Factory Control Tower")

st.subheader("1. Assets Upload")
uploaded_video = st.file_uploader("Upload Video", type=['mp4'])
uploaded_image = st.file_uploader("Upload Photo", type=['jpg', 'png'])

if st.button("Upload to GPU"):
    if uploaded_video and uploaded_image:
        files = {"video": uploaded_video, "image": uploaded_image}
        try:
            # Sab kuch 8188 par bhej rahe hain
            res = requests.post(f"{GPU_SERVER_URL}/upload", files=files, timeout=60)
            if res.status_code == 200: st.success("Upload Successful!")
            else: st.error(f"Failed: {res.status_code}")
        except Exception as e: st.error(f"Error: {e}")

st.subheader("2. Run Transformation")
if st.button("Run Viral Transformation"):
    try:
        # Transformation trigger
        res = requests.post(f"{GPU_SERVER_URL}/prompt", timeout=60)
        if res.status_code == 200: st.success("Transformation Queued!")
        else: st.error("Server Error")
    except Exception as e: st.error(f"Connection Failed: {e}")
