import streamlit as st
from yt_dlp import YoutubeDL
import os

st.title("Rijo's Youtube Video Downloader")


url = st.text_input("YouTube video URL:")


if st.button("Download"):
    if url:
        try:
            # Set download path within the current directory, there is a possibility of error here if you have different file system
            download_path = os.path.join(".", "Downloads")
            os.makedirs(download_path, exist_ok=True)

            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'verbose': True
            }

            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_title = info.get('title', 'Video')
                st.success(f"Downloaded successfully: {video_title} 😀")

               
                video_path = os.path.join(download_path, f"{video_title}.mp4")
                if os.path.exists(video_path):
                    st.write(f"")
                else:
                    st.error("Download completed, but the file path is not accessible.")

        except Exception as e:
            st.error(f"An unexpected error occurred: {e} 😔")
    else:
        st.warning("Please enter a valid YouTube URL.")
