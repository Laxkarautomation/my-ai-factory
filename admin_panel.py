import streamlit as st
import requests
import json

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

# Module A
st.header("Module A: Viral Hijacker")
uploaded_video = st.file_uploader("Upload Viral Video", type=['mp4'])
uploaded_image = st.file_uploader("Upload Avatar Photo", type=['jpg', 'png'])

if st.button("Run Viral Transformation"):
    if uploaded_video and uploaded_image:
        st.write("Sending request to GPU Server...")
        url = f"{GPU_SERVER_URL}/prompt"
        
        # FIXED PAYLOAD: Ab hum ne 'EmptyLatentImage' ko 
        # 'SaveImage' se connect kiya hai, jo ki valid link hai.
        payload = {
            "prompt": {
                "1": {
                    "inputs": {"width": 512, "height": 512, "batch_size": 1},
                    "class_type": "EmptyLatentImage"
                },
                "2": {
                    "inputs": {"samples": ["1", 0], "vae": ["4", 0]},
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
