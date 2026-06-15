import streamlit as st
import requests

# Yahan apna ngrok URL paste karein (jo abhi mila hai)
GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev"

st.title("🚀 AI Content Factory - Control Tower")

tab1, tab2 = st.tabs(["Viral Transformation", "Script-to-Video"])

with tab1:
    st.header("Module A: Viral Hijacker")
    uploaded_video = st.file_uploader("Upload Viral Video", type=['mp4'])
    uploaded_image = st.file_uploader("Upload Avatar Photo", type=['jpg', 'png'])
    
    if st.button("Run Viral Transformation"):
        if uploaded_video and uploaded_image:
            st.write("Sending request to GPU Server...")
            # Ye part FastAPI middleware se connect hoga
            st.success("Video processing started on GPU!")
        else:
            st.error("Please upload both video and image.")

with tab2:
    st.header("Module B: Script-to-Video")
    script = st.text_area("Enter your video script")
    if st.button("Generate Video"):
        st.write("Processing script...")
        # Yahan script-to-video ka logic trigger hoga
        
