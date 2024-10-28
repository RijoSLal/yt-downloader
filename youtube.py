# import streamlit as st
# from yt_dlp import YoutubeDL
# import os

# st.title("Rijo's Youtube Video Downloader")


# url = st.text_input("YouTube video URL:")


# if st.button("Download"):
#     if url:
#         try:
#             # Set download path within the current directory, there is a possibility of error here if you have different file system
#             download_path = os.path.join(".", "Downloads")
#             os.makedirs(download_path, exist_ok=True)

#             ydl_opts = {
#                 'format': 'best',
#                 'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
#                 'verbose': True
#             }

#             with YoutubeDL(ydl_opts) as ydl:
#                 info = ydl.extract_info(url, download=True)
#                 video_title = info.get('title', 'Video')
#                 st.success(f"Downloaded successfully: {video_title} 😀")

               
#                 video_path = os.path.join(download_path, f"{video_title}.mp4")
#                 if os.path.exists(video_path):
#                     st.write(f"")
#                 else:
#                     st.error("Download completed, but the file path is not accessible.")

#         except Exception as e:
#             st.error(f"An unexpected error occurred: {e} 😔")
#     else:
#         st.warning("Please enter a valid YouTube URL.")


import streamlit as st
from yt_dlp import YoutubeDL
from io import BytesIO
import tempfile
import os

st.title("Rijo's YouTube Video Downloader")

url = st.text_input("YouTube video URL:")

if st.button("Download"):
    if url:
        try:
            
            temp_dir = tempfile.gettempdir()
            ydl_opts = {
                'format': 'best',
                'noplaylist': True,
                'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s')
            }

            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_title = info.get('title', 'Video')

          
            video_file = None
            for file in os.listdir(temp_dir):
                if file.endswith('.mp4'):
                    video_file = os.path.join(temp_dir, file)
                    break

            if video_file and os.path.exists(video_file):
               
                with open(video_file, "rb") as file:
                    video_data = BytesIO(file.read())

                st.success(f"Downloaded successfully: {video_title} 😀")

              
                st.download_button(
                    label="Click here to download the video",
                    data=video_data,
                    file_name=f"{video_title}.mp4",
                    mime="video/mp4"
                )

               
                os.remove(video_file)
            else:
                st.error("The downloaded file could not be found in the temporary directory.")

        except Exception as e:
            st.error(f"An unexpected error occurred: {e} 😔")
    else:
        st.warning("Please enter a valid YouTube URL.")


