import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyBjARp9j3dMyRlsfOFoC59kI9UJX15dZ_M")

model=genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text,image_data,prompt):
    response =model.generate_content([input_text,image_data[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file was uploaded")
    
st.set_page_config(page_title="invoice_generator")
st.sidebar.header("robobill")
st.sidebar.write("made by harini")
st.sidebar.write("powered by google gemni ai")
st.header("robobill")
st.subheader("hi im  robobill")
st.subheader("manage your expenses with robobill")
input =st.text_input("what do u want me to do?",key="input")
uploaded_file=st.file_uploader("choose the image from your gallery",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="uploaded image",use_column_width=True)
ssubmit=st.button("lets go!")
input_prompt="""you are an expert in reading inc=voices.
we are going to upload an image of an image and you will have to answer any tuple of question that the user asks you.
you have to greet the user first.make sure to keep the fonts uniform ans give the items list in point wise format .
ask the user to use it again

"""
if ssubmit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.write(response)
