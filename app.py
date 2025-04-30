import streamlit as st
import cv2
from PIL import Image
import os
import helper
import base64
from streamlit_login_auth_ui.widgets import __login__
import warnings
warnings.filterwarnings("ignore")

def set_bg_hack(main_bg):
    file_extension = os.path.splitext(main_bg)[-1].lower().replace(".", "")
    with open(main_bg, "rb") as f:
        image_data = f.read()
    base64_image = base64.b64encode(image_data).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{file_extension};base64,{base64_image});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

os.makedirs("temp",exist_ok=True)

def main():
    __login__obj = __login__(auth_token = "dk_prod_XHG9DC6V4EMCB2J8X6GJA01AFJMS", 
                    company_name = "Shims",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

    LOGGED_IN = __login__obj.build_login_ui()

    if LOGGED_IN == True:
        st.title("Real-time Object Detection in Video")

        # Upload video
        video_file = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])

        if video_file:
            # Display the uploaded video
            st.video(video_file)

            # Create a button to process the video
            if st.button("Start Detection"):
                steer = cv2.imread(os.path.join('sample_data','steering_wheel_image.jpg'), 0)
                rows, cols = steer.shape
                smoothed_angle = 0
                # Save the uploaded video to a temporary location
                temp_video_path = os.path.join("temp", video_file.name)
                with open(temp_video_path, "wb") as f:
                    f.write(video_file.read())

                # Process the video in real-time
                cap = cv2.VideoCapture(temp_video_path)
                frame_idx = 0

                # Create empty placeholders for dynamic update
                input_frame_placeholder = st.empty()
                output_frame_placeholder = st.empty()
                steering_wheel_frame_placeholder = st.empty()
                text_placeholder = st.empty()

                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break

                    # Save each frame as an image
                    input_img_path = os.path.join("temp",f"frame_{frame_idx}.jpg")
                    output_img_path = os.path.join("temp",f"output_frame_{frame_idx}.jpg")

                    cv2.imwrite(input_img_path, frame)

                    # Call the object detection function
                    detected_text = helper.get_results(input_img_path, output_img_path)

                    smoothed_angle += 0.2 * pow(abs((detected_text['detected_angle'] - smoothed_angle)), 2.0 / 3.0) * (detected_text['detected_angle'] - smoothed_angle) / abs(detected_text['detected_angle'] - smoothed_angle)
                    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -smoothed_angle, 1)
                    dst = cv2.warpAffine(steer, M, (cols, rows))

                    # Load the output image
                    output_image = Image.open(output_img_path)
                    # Update the placeholders with the new content
                    input_frame_placeholder.image(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR), caption=f"Input Frame {frame_idx}", width=None)
                    output_frame_placeholder.image(output_image, caption=f"Output Frame {frame_idx}", width=None)
                    steering_wheel_frame_placeholder.image(dst, caption="steering wheel", width=None)
                    text_placeholder.write(detected_text)  # Display the text returned by detect_object

                    frame_idx += 1

                    os.remove(input_img_path)
                    os.remove(output_img_path)

                cap.release()

if __name__ == "__main__":
    main()

#steering wheel image
#distance calculation
#login
#trim to signal