import streamlit as st 
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

 
model=load_model('cnn_model.h5')
 

def process_image(img):
    img=img.resize((170,170))
    img=np.array(img)
    img=img/255.0 #normalize
    img=np.expand_dims(img,axis=0)
    return img

st.title("Cancer Image Classification :cancer:")
st.write("Select image and model predicts whether it is cancer")
         
file=st.file_uploader('Bir Resim Sec',type=['jpg','jpeg','png'])

if file is not None:
    img=Image.open(file)
    st.image(img,caption='uploaded image')
    image= process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)

    class_names=['Non Cancer','Cancer']

    st.write(class_names[predicted_class])