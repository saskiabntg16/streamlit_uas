import streamlit as st
import pandas as pd
from PIL import Image

st.write("""
# UAS DWDM Deploy Klasifikasi Iris Menggunakan Streamlit
Nama: Saskia Bintang Maharani
NIM : 2019230047
"""
)

img = Image.open ('iris.png')
st.image(img, use_column_width=False)

st.sidebar.header('Parameter Value')

def input_user():
    SepalLengthCm = st.slider('SepalLengthCm:', 2.0, 6.0)
    SepalWidthCm = st.slider('SepalWidthCm:', 0.0, 5.0)
    PetalLengthCm = st.slider('PetalLengthCm',0.0, 3.0)
    PetalWidthCm = st.slider('PetalWidthCm:', 0.0, 2.0)

data = {'SepalLengthCm': SepalLengthCm,
            'SepalWidthCm': SepalWidthCm,
            'PetalLengthCm': PetalLengthCm,
            'PetalWidthCm': PetalWidthCm}
     
fitur = pd.DataFrame(data, index=[0])
