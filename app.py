import streamlit as st
import pandas as pd
from PIL import Image
from sklearn import datasets
from sklearn.svm import SVC
import pickle 

st.write("""
# WebApp Klasifikasi Iris Menggunakan Streamlit
Nama: **Saskia Bintang Maharani**  |   NIM : **2019230047**
"""
)

img = Image.open ('iris.png')
st.image(img, use_column_width=False)

st.sidebar.header('Parameter Value')

def input_user():
SepalLengthCm = st.sidebar.slider('SepalLengthCm:', 4.3, 7.9, 5.4)
SepalWidthCm = st.sidebar.slider('SepalWidthCm:', 2.0, 4.4, 3.4)
PetalLengthCm = st.sidebar.slider('PetalLengthCm', 1.0, 6.9, 1.3)
PetalWidthCm = st.sidebar.slider('PetalWidthCm:', 0.1, 2.5, 0.2)

data = {'Sepal Length': SepalLengthCm,
        'Sepal Width': SepalWidthCm,
        'Petal Length': PetalLengthCm,
        'Petal Width': PetalWidthCm}
     
features = pd.DataFrame(data, index=[0]) 
return features

df = input_user()
