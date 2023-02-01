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
return fitur

df = input_user()

dt.subheader('Parameter Inputan')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target
model = SVC()
model.fit(X,Y)

model = pickle.load(open('model.pkl', 'rb'))
prediksi = model.predict(df)
prediksi_proba = model.predict.proba(df)

st.subheader('Label Kelas dan Nomor Indeks Sesuai Inputan')
st.write(iris.target_names)

st.subheader('Prediksi (Hasil Klasifikasi)')
st.write(iris.target_names[prediksi])

st.subheader('Probabilitas Hasil Predikasi(klasifikasi)')
st.write(predikasi_proba)

st.subheader('Prediction Percentages:') 
st.write('**Probablity of Iris Class being Iris-setosa is ( in % )**:',pred_proba[0][0]*100)
st.write('**Probablity of Isis Class being Iris-versicolor is ( in % )**:',pred_proba[0][1]*100)
st.write('**Probablity of Isis Class being Iris-virginica ( in % )**:',pred_proba[0][2]*100)
