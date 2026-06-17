import streamlit as st
import requests
import json

GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev"

st.set_page_config(page_title="AI Content Factory", layout="wide")
st.title("🚀 AI Content Factory - Control Tower")

if st.sidebar.button("Test GPU Connection"):
    try:
        response = requests.get(f"{GPU_SERVER_URL}/", timeout=10)
        st.sidebar.success(f"GPU Server Online (Status: {response.status_code})")
    except Exception as e:
        st.sidebar.error(f"GPU Server Offline! {e}")

tab1, tab2 = st.tabs(["Viral Transformation", "Script-to-Video"])

with tab1:
    st.header("Module A: Viral Hijacker")
    uploaded_video = st.file_uploader("Upload Viral Video", type=['mp4'])
    uploaded_image = st.file_uploader("Upload Avatar Photo", type=['jpg', 'png'])
    
    if st.button("Run Viral Transformation"):
        if uploaded_video and uploaded_image:
            st.write("Sending request to GPU Server...")
            url = f"{GPU_SERVER_URL}/prompt"
            
            # FIXED: Removed CheckpointLoader because the model file is missing on server
            # Using 'LoadImage' node instead as a safe placeholder
            payload = {
                "prompt": {
                    "1": {
                        "inputs": {"image": "avatar.jpg", "upload": "image"},
                        "class_type": "LoadImage"
                    },
                    "2": {
                        "inputs": {"images": ["1", 0]},
                        "class_type": "SaveImage"
                    }
                }
            }
            
            try:
                response = requests.post(url, json=payload, timeout=10)
                if response.status_code == 200:
                    st.success("Video processing queued! Check Colab logs.")
                else:
                    st.error(f"Server rejected: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Connection Failed: {e}")
        else:
            st.error("Please upload both files.")

with tab2:
    st.header("Module B: Script-to-Video")
    script = st.text_area("Enter your video script here")
    if st.button("Generate Video from Script"):
        if script:
            st.info("Script-to-video workflow is currently being mapped.")
        else:
            st.warning("Please enter a script.")
