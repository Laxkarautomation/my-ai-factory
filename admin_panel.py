import streamlit as st
import requests
import json

# URL update kar lena jo aaj Colab se mila hai
GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev"

st.set_page_config(page_title="AI Content Factory", layout="wide")
st.title("🚀 AI Content Factory - Control Tower")

# Test Connection
if st.sidebar.button("Test GPU Connection"):
    try:
        response = requests.get(f"{GPU_SERVER_URL}/", timeout=10)
        st.sidebar.success(f"GPU Server Online (Status: {response.status_code})")
    except Exception as e:
        st.sidebar.error(f"GPU Server Offline! {e}")

# Module Tabs
tab1, tab2 = st.tabs(["Viral Transformation", "Script-to-Video"])

with tab1:
    st.header("Module A: Viral Hijacker")
    uploaded_video = st.file_uploader("Upload Viral Video", type=['mp4'])
    uploaded_image = st.file_uploader("Upload Avatar Photo", type=['jpg', 'png'])
    
    if st.button("Run Viral Transformation"):
        if uploaded_video and uploaded_image:
            st.write("Sending request to GPU Server...")
            url = f"{GPU_SERVER_URL}/prompt"
            
            # FIXED PAYLOAD: VAE Index 2 se linked hai
            payload = {
                "prompt": {
                    "1": {
                        "inputs": {"width": 512, "height": 512, "batch_size": 1},
                        "class_type": "EmptyLatentImage"
                    },
                    "2": {
                        "inputs": {
                            "samples": ["1", 0], 
                            "vae": ["4", 2] 
                        },
                        "class_type": "VAEDecode"
                    },
                    "3": {
                        "inputs": {"filename_prefix": "Viral_Output", "images": ["2", 0]},
                        "class_type": "SaveImage"
                    },
                    "4": {
                        "inputs": {"ckpt_name": "v1-5-pruned.ckpt"},
                        "class_type": "CheckpointLoaderSimple"
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
