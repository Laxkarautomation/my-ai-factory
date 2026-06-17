import streamlit as st
import requests

GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev"

st.set_page_config(page_title="AI Content Factory", layout="wide")
st.title("🚀 AI Content Factory - Control Tower")

# Upload Module
st.header("Upload Assets to Factory")
uploaded_video = st.file_uploader("Upload Viral Video", type=['mp4'])
uploaded_image = st.file_uploader("Upload Avatar Photo", type=['jpg', 'png'])

if st.button("Upload to GPU Server"):
    if uploaded_video and uploaded_image:
        files = {
            "video": uploaded_video.getvalue(),
            "image": uploaded_image.getvalue()
        }
        # Files ko server ke input folder mein push karenge
        response = requests.post(f"{GPU_SERVER_URL}/upload", files=files)
        if response.status_code == 200:
            st.success("Assets uploaded to Input folder!")
        else:
            st.error("Upload failed!")

if st.button("Run Viral Transformation"):
    url = f"{GPU_SERVER_URL}/prompt"
    payload = {
        "prompt": {
            "1": {"inputs": {"image": "avatar.jpg"}, "class_type": "LoadImage"},
            "2": {"inputs": {"filename_prefix": "Viral", "images": ["1", 0]}, "class_type": "SaveImage"}
        }
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        st.success("Processing queued!")
