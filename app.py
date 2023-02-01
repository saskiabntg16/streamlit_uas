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
SepalLengthCm=st.sidebar.slider('Sepal Length:', 2.0, 6.0)

df = input_user()
