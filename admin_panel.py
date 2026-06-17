import streamlit as st
import requests

# Yahan apna wahi ngrok URL paste karo jo tumhein Colab se mila tha
GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev/"

st.set_page_config(page_title="AI Content Factory", layout="wide")
st.title("🚀 AI Content Factory - Control Tower")

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
            # Connection check
            try:
                # ComfyUI prompt endpoint
                response = requests.post(f"{GPU_SERVER_URL}/prompt", json={"prompt": {}}) 
                if response.status_code == 200:
                    st.success("Video processing queued! Check Colab logs.")
                else:
                    st.error(f"Server rejected: {response.text}")
            except Exception as e:
                st.error(f"Connection Failed: {e}")
        else:
            st.error("Please upload both video and image.")

# Module B: Script-to-Video
with tab2:
    st.header("Module B: Script-to-Video")
    script = st.text_area("Enter your video script here")
    voice_style = st.selectbox("Select Voice Style", ["Professional", "Energetic", "Casual"])
    
    if st.button("Generate Video from Script"):
        if script:
            st.write(f"Generating video for: {voice_style} style...")
            # Yahan middleware logic aayega jo script ko process karega
            st.success("Task queued for script generation!")
        else:
            st.warning("Please enter a script.")

# Connection Test Sidebar
st.sidebar.header("System Status")
if st.sidebar.button("Test GPU Connection"):
    try:
        response = requests.get(GPU_SERVER_URL)
        st.sidebar.success(f"GPU Server Online (Status: {response.status_code})")
    except Exception:
        st.sidebar.error("GPU Server Offline! Check Colab.")
        
