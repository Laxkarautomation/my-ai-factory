import streamlit as st
import requests
import json

# Yahan apna wahi ngrok URL paste karo jo tumhein Colab se mila tha
GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev"

st.set_page_config(page_title="AI Content Factory", layout="wide")
st.title("🚀 AI Content Factory - Control Tower")

# Sidebar: Connection Test
st.sidebar.header("System Status")
if st.sidebar.button("Test GPU Connection"):
    try:
        # Check root to see if server is online
        response = requests.get(f"{GPU_SERVER_URL}/", timeout=10)
        st.sidebar.success(f"GPU Server Online (Status: {response.status_code})")
    except Exception as e:
        st.sidebar.error(f"GPU Server Offline! Check Colab: {e}")

# Tab Selection
tab1, tab2 = st.tabs(["Viral Transformation", "Script-to-Video"])

# Module A: Viral Hijacker
with tab1:
    st.header("Module A: Viral Hijacker")
    uploaded_video = st.file_uploader("Upload Viral Video", type=['mp4'])
    uploaded_image = st.file_uploader("Upload Avatar Photo", type=['jpg', 'png'])
    
    if st.button("Run Viral Transformation"):
        if uploaded_video and uploaded_image:
            st.write("Sending request to GPU Server...")
            
            # ComfyUI API endpoint for queuing prompts
            url = f"{GPU_SERVER_URL}/prompt"
            
            # IMPORTANT: Yahan par tumhara workflow ka JSON payload aayega
            # Abhi hum basic structure bhej rahe hain
            payload = {
                "prompt": {
                    # Yahan tumhare ComfyUI nodes ki details aayengi
                }
            }
            
            try:
                # ComfyUI API requires POST requests
                response = requests.post(url, json=payload, timeout=10)
                
                if response.status_code == 200:
                    st.success("Video processing queued! Check Colab logs.")
                else:
                    st.error(f"Server rejected: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Connection Failed: {e}")
        else:
            st.error("Please upload both video and image.")

# Module B: Script-to-Video
with tab2:
    st.header("Module B: Script-to-Video")
    script = st.text_area("Enter your video script here")
    
    if st.button("Generate Video from Script"):
        if script:
            st.info("Script-to-video workflow is currently being mapped.")
        else:
            st.warning("Please enter a script.")
