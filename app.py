import streamlit as st
import pandas as pd
import pickle
from PIL import Image
from sklearn import datasets
from sklearn.svm import SVC

model = pickle.load(open('model.pkl', 'rb'))

st.header("IRIS CLASSIFICATION PREDICTION")
st.write("NAMA : SASKIA BINTANG MAHARANI")
st.write("NIM : 2019230047")

img = Image.open ('iris.png')
st.image(img, use_column_width=False)
st.write("Please Insert Values, to Get Iris Class prediction:")

st.sidebar.header('Parameter Value Prediction')

SepalLengthCm = st.sidebar.slider('SepalLengthCm:', 2.0, 6.0)
SepalWidthCm = st.sidebar.slider('SepalWidthCm:', 0.0, 5.0)
PetalLengthCm = st.sidebar.slider('PetalLengthCm',0.0, 3.0)
PetalWidthCm = st.sidebar.slider('PetalWidthCm:', 0.0, 2.0)
data = {'SepalLengthCm': SepalLengthCm,
        'SepalWidthCm': SepalWidthCm,
        'PetalLengthCm': PetalLengthCm,
        'PetalWidthCm': PetalWidthCm}

features = pd.DataFrame(data, index=[0])

species = {'Iris Setosa', 'Iris Versicolor', 'Iris Virginica'}

st.subheader('Parameter Inputan')
st.write(features)

iris = datasets.load_iris()
X = iris.data
Y = iris.species
model = SVC()
model.fit(X,Y)

model = pickle.load(open('model.pkl', 'rb'))
prediksi = model.predict(features)
prediksi_proba = model.predict_proba(features)

st.subheader('Label Kelas dan Nomor Indeks Sesuai Inputan')
st.write(iris.species)

st.subheader('Prediksi (Hasil Klasifikasi)')
st.write(iris.species[prediksi])

st.subheader('Probabilitas Hasil Predikasi(klasifikasi)')
st.write(prediksi_proba)

st.subheader('Prediction Percentages:') 
st.write('**Probablity of Iris Class being Iris-setosa is ( in % )**:',pred_proba[0][0]*100)
st.write('**Probablity of Isis Class being Iris-versicolor is ( in % )**:',pred_proba[0][1]*100)
st.write('**Probablity of Isis Class being Iris-virginica ( in % )**:',pred_proba[0][2]*100)
