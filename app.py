import streamlit as st
import requests
import time

st.set_page_config(page_title="AI Content Factory", layout="centered")

st.title("AI Content Factory")
st.caption("Streamlit → Colab FastAPI → ComfyUI → Final Output")

backend_url = st.text_input(
    "Colab Ngrok Backend URL",
    placeholder="https://wobble-roast-numerate.ngrok-free.dev"
)

video_file = st.file_uploader("Upload video", type=["mp4", "mov", "webm"])
image_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg", "webp"])

if st.button("Generate", type="primary"):
    if not backend_url:
        st.error("Paste your Ngrok backend URL first.")
        st.stop()

    if not video_file or not image_file:
        st.error("Upload both video and image.")
        st.stop()

    backend_url = backend_url.rstrip("/")

    with st.spinner("Checking backend..."):
        try:
            health = requests.get(f"{backend_url}/health", timeout=20)
            if health.status_code != 200:
                st.error("Backend health check failed.")
                st.stop()
        except Exception as e:
            st.error(f"Backend not reachable: {e}")
            st.stop()

    files = {
        "video": (video_file.name, video_file.getvalue(), video_file.type),
        "image": (image_file.name, image_file.getvalue(), image_file.type),
    }

    with st.spinner("Generating... this can take time on Colab."):
        try:
            res = requests.post(
                f"{backend_url}/generate",
                files=files,
                timeout=1200
            )

            if res.status_code != 200:
                st.error(res.text)
                st.stop()

            data = res.json()
            job_id = data["job_id"]

            result_url = f"{backend_url}/result/{job_id}"
            output = requests.get(result_url, timeout=300)

            if output.status_code != 200:
                st.error(output.text)
                st.stop()

            content_type = output.headers.get("content-type", "")

            st.success("Generation complete.")

            if "video" in content_type or result_url.endswith((".mp4", ".mov", ".webm")):
                st.video(output.content)
                st.download_button(
                    "Download Output",
                    data=output.content,
                    file_name="ai_output.mp4"
                )
            else:
                st.image(output.content)
                st.download_button(
                    "Download Output",
                    data=output.content,
                    file_name="ai_output.png"
                )

        except Exception as e:
            st.error(f"Generation failed: {e}")
