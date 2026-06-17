import streamlit as st
import requests

GPU_SERVER_URL = "https://wobble-roast-numerate.ngrok-free.dev/"

st.title("🚀 AI Control Tower - Debug Mode")

uploaded_video = st.file_uploader("Upload Video", type=['mp4'])
uploaded_image = st.file_uploader("Upload Photo", type=['jpg', 'png'])

if st.button("Upload to GPU"):
    if uploaded_video and uploaded_image:
        files = {"video": uploaded_video, "image": uploaded_image}
        # Debugging: URL print karo taaki pata chale kahan bhej rahe ho
        upload_url = GPU_SERVER_URL.replace('8188', '5001') + "/upload"
        st.write(f"Sending to: {upload_url}")
        
        try:
            res = requests.post(upload_url, files=files, timeout=30)
            if res.status_code == 200:
                st.success("Success!")
            else:
                st.error(f"Failed! Status Code: {res.status_code}")
                st.text(res.text) # Ye batayega ki error kya hai
        except Exception as e:
            st.error(f"Connection Error: {e}")
