import streamlit as st
import requests

GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev/"

st.title("🚀 AI Factory Control Tower")

uploaded_video = st.file_uploader("Upload Video", type=['mp4'])
uploaded_image = st.file_uploader("Upload Photo", type=['jpg', 'png'])

if st.button("Upload to GPU"):
    if uploaded_video and uploaded_image:
        files = {"video": uploaded_video, "image": uploaded_image}
        try:
            # Request seedha ngrok URL (8188) par bhej rahe hain
            res = requests.post(f"{GPU_SERVER_URL}/upload", files=files, timeout=60)
            if res.status_code == 200: st.success("Upload Successful!")
            else: st.error(f"Upload Failed: {res.status_code}")
        except Exception as e: st.error(f"Connection Error: {e}")
