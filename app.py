import streamlit as st
from PIL import Image

def main():
    st.title("Driver Distraction Model")

    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # You might need to fix the import statement for InferenceHTTPClient
        from inference_sdk import InferenceHTTPClient

        CLIENT = InferenceHTTPClient(
            api_url="https://detect.roboflow.com",
            api_key="Ps51nXOB4N8owuxwYi4n"
        )

        result = CLIENT.infer(image, model_id="distracted-drivers/1")
        objects = []
        for i in result['predictions']:
            objects.append(i['class'])
        
        st.write("The following objects are detected in the image:", objects)

        distraction = False
        if "HandsNotOnWheel" in objects:
            distraction = True
        if "Mobiles" in objects:
            distraction = True
        if "close_eye" in objects:
            distraction = True
        if "drowsy" in objects:
            distraction = True
        if "close_eye" in objects:
            distraction = True
          
        if distraction:
            st.warning("The driver seems distracted")
        else:
            st.success("The driver is not distracted")

if __name__ == "__main__":
    main()
