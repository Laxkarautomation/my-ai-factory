import streamlit as st

st.title("🚀 AI Content Factory")
tab1, tab2 = st.tabs(["Viral Transformation", "Script-to-Video"])

with tab1:
    st.header("Module A: Viral Hijacker")
    video_file = st.file_uploader("Upload Viral Video", type=['mp4'])
    image_file = st.file_uploader("Upload Avatar Photo", type=['jpg', 'png'])
    if st.button("Run Viral Transformation"):
        st.write("Triggering GPU Pipeline...")

with tab2:
    st.header("Module B: Script-to-Video")
    script = st.text_area("Enter your script")
    if st.button("Generate Video"):
        st.write("Generating script-to-video...")
      
